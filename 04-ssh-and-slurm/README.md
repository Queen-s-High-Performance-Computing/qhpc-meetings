# Meeting 04: SSH and Slurm on the CAC

Connect to the CAC, use Vim to create a job script in `~/qhpc`, submit it with Slurm,
and then submit the STREAM memory bandwidth benchmark and use the roofline model to
judge what the result means.

## Prerequisites

### Software and access

- On macOS or Linux, open **Terminal**. On Windows, open **Windows Terminal** with **WSL** or **Git Bash**.
- An active CAC account.
- A text editor on your computer; the activity uses Vim to edit the job script on the CAC.
- A C compiler on the CAC (check with `gcc --version` after connecting; it ships on the CAC login nodes).

### Core skills and guides

- [Using the Linux CLI](../guides/using-the-linux-cli.md)
- **SSH keys:** [Create or reuse an SSH key](../guides/ssh-keys.md#1-create-or-reuse-a-key).
- **Text editing:** [Meeting 03: Vim and nano](../03-linux-vms-and-containers/README.md#text-editors-vim-and-nano). Practice entering text, saving, and quitting Vim if these are unfamiliar.

## 1. Configure SSH to the CAC

SSH opens a terminal session on another computer. Find your username in the top-right corner of the CAC account portal:

![CAC account portal with the username highlighted in the top-right corner](resources/image.png)

On **your computer**, open `~/.ssh/config` in your preferred editor. For example:

**Bash (macOS / Linux / WSL / Git Bash):**

```bash
vim ~/.ssh/config
```

Keep existing entries and add the block below near the start. Replace `YOUR_CAC_USERNAME` with your username and adjust `IdentityFile` if you used another key filename.

```sshconfig
Host cac
    HostName login.cac.queensu.ca
    User YOUR_CAC_USERNAME
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    AddKeysToAgent yes
    IgnoreUnknown UseKeychain
    UseKeychain yes  # macOS only
```

`Host` is your shortcut; `HostName` and `User` identify the server and account. The key settings select your key and allow caching through a running SSH agent. `IgnoreUnknown` lets other platforms skip the macOS Keychain option.

Register your public key once. Run the appropriate commands **on your computer**, adjusting the `.pub` path if needed.

**Bash (macOS / Linux / WSL / Git Bash)**, with `ssh-copy-id` installed:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub cac
```

If `ssh-copy-id` is unavailable, use this Bash alternative:

```bash
cat ~/.ssh/id_ed25519.pub |
    ssh cac "umask 077; mkdir -p ~/.ssh; tr -d '\r' >> ~/.ssh/authorized_keys"
```

Connect using your shortcut:

```bash
ssh cac
```

On your first connection, confirm the host fingerprint using CAC guidance before accepting it. Follow the CAC authentication prompts; passwords and key passphrases do not appear as you type.

### Optional: reuse an authenticated connection

**macOS / Linux / WSL only.**

**Connection multiplexing** lets later `ssh cac` sessions from your computer reuse an existing connection without repeating the password and 2FA prompts. The first connection still authenticates normally.

Add these lines inside your existing `Host cac` block in `~/.ssh/config`:

```sshconfig
    ControlMaster auto
    ControlPath ~/.ssh/control-%C
    ControlPersist 1h
```

The shared connection stays available for up to one hour after the last session closes. If it disconnects or expires, the next connection authenticates again.

When finished, run `ssh -O exit cac` **on your computer** to close the shared connection and any attached sessions.

## 2. Create a job script on the CAC

After `ssh cac`, every platform uses the same Linux commands (bash) **on the CAC**, inside the SSH session:

```bash
# This is all bash now
mkdir -p ~/qhpc
cd ~/qhpc
vim hello.slurm
```

Vim is a terminal text editor. Press **i** to enter Insert mode, then paste (try typing it for fun :D):

*Use vimtutor if you need a refresher, or use this vim [cheat sheet](https://vim.rtorr.com).*

```bash
#!/bin/bash
#SBATCH --job-name=qhpc-hello
#SBATCH --ntasks=1
#SBATCH --time=00:01:00
#SBATCH --mem=256M
#SBATCH --output=hello-%j.out

echo "Hello from job $SLURM_JOB_ID"
hostname
date

echo
echo "--- Allocation ---"
echo "Partition: $SLURM_JOB_PARTITION"
echo "Node(s): $SLURM_JOB_NODELIST"
echo "CPUs on this node: $SLURM_CPUS_ON_NODE"
echo "Memory per node: $SLURM_MEM_PER_NODE MB"

echo
echo "--- CPU ---"
lscpu | grep -E "Model name|^CPU\(s\)|Thread|Core"

echo
echo "--- GPU ---"
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi --query-gpu=name,memory.total --format=csv
else
    echo "No GPU tools found on this node (this job did not request a GPU)."
fi
```

Press **Esc**, type `:wq`, and press **Enter** to save and quit. To quit without saving, use `:q!` instead.

Slurm schedules work on compute nodes. The `#SBATCH` lines request one task, one minute, and 256 MiB of memory. `%j` becomes the job ID in the output filename. Account and partition use the CAC defaults. The rest of the script prints what Slurm actually handed you for this job: which node, how many CPUs, how much memory, and whether a GPU is attached — this is the resource allocation behind "running an application on the cluster."

## 3. Submit and inspect the job

From `~/qhpc` on the CAC:

```bash
sbatch hello.slurm
```

Expect `Submitted batch job` followed by a number. Use that number in place of `JOBID` below:

```bash
squeue -j JOBID
```

`PD` means pending; `R` means running. A short job may finish before you see it in the queue. After it finishes:

```bash
sacct -j JOBID --format=JobID,State,ExitCode,Elapsed
cat hello-JOBID.out
```

Look for `COMPLETED`, exit code `0:0`, and output containing your job ID, a compute-node hostname, a date, and the allocation/CPU/GPU details. Accounting results may take a moment to appear.

To cancel this job while pending or running, use `scancel JOBID`. Keep your script for later; remove its output with `rm hello-JOBID.out` when finished.

**Try next:** Change the greeting, submit again, and compare the two output files.

## 4. Build and submit the STREAM benchmark

The CPU, memory, and GPU details above describe what you were *given*; STREAM measures
how fast that allocation can actually move data.

On **your computer**, open [`stream.c`](https://www.cs.virginia.edu/stream/FTP/Code/stream.c)
directly (the other files in that [directory](https://www.cs.virginia.edu/stream/FTP/Code/)
are for the Fortran version and other variants; the C version is self-contained). Your
browser will likely display it as plain text instead of offering a download — save it
with your browser's save-page shortcut (**Ctrl+S** / **Cmd+S**), keeping the filename
`stream.c` and the format set to **All Files** / **Page Source**, not **Web Page, HTML only**.
Then copy it to the CAC using your SSH shortcut:

```bash
scp stream.c cac:~/qhpc/stream.c
```

Back **on the CAC**, compile it:

```bash
cd ~/qhpc
gcc -O3 stream.c -o stream
```

Create the job script:

```bash
vim stream.slurm
```

```bash
#!/bin/bash
#SBATCH --job-name=qhpc-stream
#SBATCH --ntasks=1
#SBATCH --time=00:05:00
#SBATCH --mem=1G
#SBATCH --output=stream-%j.out

./stream
```

Save and quit (`:wq`), then submit it from `~/qhpc`:

```bash
sbatch stream.slurm
```

Use the job number from `Submitted batch job` in place of `JOBID`:

```bash
squeue -j JOBID
sacct -j JOBID --format=JobID,State,ExitCode,Elapsed
cat stream-JOBID.out
```

Look for `COMPLETED` and exit code `0:0`. Use `scancel JOBID` to cancel a pending or
running job; use `exit` to end the SSH session when done.

## 5. Why STREAM?

STREAM runs four simple kernels over large arrays, each moving data between memory
and the CPU without doing much math per byte:

| Kernel | Operation | Bytes moved per element |
| --- | --- | --- |
| Copy | `a[i] = b[i]` | 16 |
| Scale | `a[i] = q * b[i]` | 16 |
| Add | `a[i] = b[i] + c[i]` | 24 |
| Triad | `a[i] = b[i] + q * c[i]` | 24 |

Most real applications spend as much time waiting on memory as doing arithmetic, but
that bottleneck rarely shows up when you only look at a CPU's advertised FLOP/s.
STREAM's job is to measure the other half: how fast a node can actually move data,
independent of any specific application. **Triad** is the standard number to cite, and
it is what you will compare against in the next two sections.

## 6. Reading the output

A run prints a block like this (numbers vary by node):

```
Function    Best Rate MB/s  Avg time     Min time     Max time
Copy:           14201.3     0.011408     0.011267     0.011622
Scale:          14159.8     0.011341     0.011299     0.011410
Add:            15872.4     0.015129     0.015121     0.015142
Triad:          15844.7     0.015160     0.015150     0.015171
```

Take the **Min time** column (the fastest of several repeated trials — the one least
disturbed by other activity on the node) and its matching **Best Rate**. Higher MB/s
is better. The Triad rate is the number to carry into the roofline model below.

## 7. The roofline model: is this fast?

The [roofline model](https://en.wikipedia.org/wiki/Roofline_model) plots a chip's
achievable performance (GFLOP/s) against a kernel's **arithmetic intensity**
(floating-point operations per byte moved). It has two roofs:

- A flat **compute roof**, at the chip's peak FLOP/s — you can never do more math per
  second than this, no matter how intense the kernel.
- A slanted **memory roof**, whose slope is the memory bandwidth you just measured
  with STREAM — you can never move data faster than this, no matter how little math
  you do per byte.

The point where they meet is the **ridge point**: kernels to its left (low arithmetic
intensity) are memory-bound and sit on the slanted roof; kernels to its right are
compute-bound and sit on the flat roof. Triad's arithmetic intensity is tiny — 2 flops
for 24 bytes — so it always lands deep on the memory roof. That is the point: STREAM
is not meant to run fast, it is meant to measure the slope of that roof so you have a
real number, instead of a spec-sheet number, for what "memory-bound" means on this
node.

With your Triad rate from STREAM and the node's peak FLOP/s (from the
[CAC cluster documentation](https://cac.queensu.ca/systems/traditional-hpc/) or the
vendor spec sheet), you can sketch your own roofline chart and see, for any
application, whether it is closer to the memory roof or the compute roof — and
therefore which one is worth optimizing.

**Try next:** Re-run with a larger array (`gcc -O3 -DSTREAM_ARRAY_SIZE=40000000 stream.c -o stream`)
or try the OpenMP version of STREAM with multiple `--cpus-per-task` to see the Triad
rate climb closer to the node's full memory bandwidth.

## Resources

- [CAC cluster information and documentation](https://cac.queensu.ca/systems/traditional-hpc/).
- [OpenSSH client configuration](https://man.openbsd.org/ssh_config): host settings, keys, and connection multiplexing; [SSH control commands](https://man.openbsd.org/ssh.1#O).
- [ssh-copy-id manual](https://github.com/openssh/openssh-portable/blob/master/contrib/ssh-copy-id.1): register your public key on a remote server.
- [Apple's SSH Keychain settings](https://developer.apple.com/library/archive/technotes/tn2449/_index.html): `UseKeychain` and `AddKeysToAgent`.
- [Vim: first steps](https://vimhelp.org/usr_02.txt.html): editing, saving, and quitting.
- [Slurm quick start](https://slurm.schedmd.com/quickstart.html); command references: [sbatch](https://slurm.schedmd.com/sbatch.html), [squeue](https://slurm.schedmd.com/squeue.html), [sacct](https://slurm.schedmd.com/sacct.html), and [scancel](https://slurm.schedmd.com/scancel.html).
- [STREAM homepage](https://www.cs.virginia.edu/stream/): benchmark source, run rules, and published results.
- [Roofline model introduction](https://crd.lbl.gov/divisions/amcr/computer-science-amcr/par/research/roofline/introduction) (Lawrence Berkeley National Laboratory).
