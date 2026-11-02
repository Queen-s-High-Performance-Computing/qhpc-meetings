# Meeting 05: Profiling and Optimization

Practise the measure-first routine from the lecture on a small C program on the CAC:
get a baseline time, try compiler flags, profile to find the hot spot, then make one
change and measure again. The same routine is how to start on DOOMATHON.

## Prerequisites

### Software and access

- On macOS or Linux, open **Terminal**. On Windows, open **Windows Terminal** with **WSL** or **Git Bash**.
- An active CAC account and the `cac` SSH shortcut from [Meeting 04](../04-stream-benchmark-on-cac/README.md#1-configure-ssh-to-the-cac).
- GCC and `perf` on the CAC. Both are available on the login nodes; after `ssh cac`, check with:

  ```bash
  command -v gcc perf
  ```

  Each prints a path. If either is missing, ask in the club channel. Use the CAC even if you have a C compiler on your computer, so everyone's numbers come from the same kind of machine.

### Core skills and guides

- [Using the Linux CLI](../guides/using-the-linux-cli.md)
- **Slurm jobs:** [Meeting 04: submit and inspect a job](../04-stream-benchmark-on-cac/README.md#3-submit-and-inspect-the-job) (`sbatch`, `squeue`, `sacct`).
- **Text editing:** [Meeting 03: Vim and nano](../03-linux-vms-and-containers/README.md#text-editors-vim-and-nano).

## The routine

| Step | What you do | Why |
| --- | --- | --- |
| 1. Baseline | Build without optimization and time a realistic run, several times | Every later number is compared against this one |
| 2. Compiler flags | Rebuild with `-O2` or `-O3` and check the output still matches | Free speed, when it works |
| 3. Profile | Use a profiler to see which functions take the time | Guesses about the slow part are often wrong |
| 4. Change one thing | Fix the hot spot, then go back to step 1's measurement | Some changes make things slower |

## 1. Get the sample onto the CAC

The sample program, [`hotspot.c`](samples/hotspot.c), fills a 4096 × 4096 grid of whole
numbers (128 MiB) and adds it up in two different functions, ten times over. It prints two
totals; those are your check that a change didn't break anything. The job script
[`time-runs.slurm`](samples/time-runs.slurm) runs a program three times in a row on a
compute node and times each run.

On **your computer**, open each file above on GitHub, choose **Download raw file**, and
copy both to the CAC (adjust the paths if your browser saved them somewhere else):

```bash
ssh cac "mkdir -p ~/qhpc/05"
scp ~/Downloads/hotspot.c ~/Downloads/time-runs.slurm cac:~/qhpc/05/
```

Everything from here on runs **on the CAC**, after `ssh cac`:

```bash
cd ~/qhpc/05
```

## 2. Get a baseline

Build with no optimization (`-O0`) and with debug information (`-g`), then submit the
timing job:

```bash
gcc -O0 -g -o hotspot-O0 hotspot.c
sbatch time-runs.slurm ./hotspot-O0
```

Expect `Submitted batch job` and a number. When `squeue -j JOBID` no longer lists it, read
the output:

```bash
cat time-runs-JOBID.out
```

Each run prints the two totals followed by three times:

- **real:** wall-clock time, how long you actually waited.
- **user:** CPU time spent running your code.
- **sys:** CPU time spent in the operating system on your behalf.

Write down the totals and the typical `real` time. The three runs won't match exactly;
that spread is normal on a shared cluster, so compare typical values rather than your
single best.

## 3. Try compiler flags

Build two optimized versions and time each one:

```bash
gcc -O2 -g -o hotspot-O2 hotspot.c
gcc -O3 -g -o hotspot-O3 hotspot.c
sbatch time-runs.slurm ./hotspot-O2
sbatch time-runs.slurm ./hotspot-O3
```

Check that the totals match your baseline exactly, then compare the times.

Don't be surprised if the improvement is smaller than you expected. On Frontenac, `-O2`
and `-O3` each cut the time by only about 10% (from about 2.9 s to about 2.7 s), and the
optimized runs varied by up to 0.3 s from run to run. That's a clue: the compiler made the
arithmetic faster, so something other than arithmetic must be taking most of the time.

## 4. Profile with perf

`perf record` samples your program while it runs: many times a second, it notes which
function the CPU is in. It needs no special build; the `-g` you already used lets it show
function names. Run it on a compute node with your `-O2` build; it writes a file called
`perf.data` in `~/qhpc/05`:

```bash
sbatch --time=00:05:00 --mem=1G --output=perf-record-%j.out \
  --wrap="perf record -o perf.data ./hotspot-O2"
```

`--wrap` turns a single command into a job, so you don't need a script for it. After the
job finishes, read the report (this is light work, so the login node is fine):

```bash
perf report -i perf.data --stdio 2>/dev/null | grep -v '^#' | head -10
```

Each line shows the share of samples, the program, where the code lives, and the function
name, from most to least time. On Frontenac the top of the report looked like this (your
numbers will differ a little):

```
    93.45%  hotspot-O2  hotspot-O2                [.] column_sum
     5.87%  hotspot-O2  hotspot-O2                [.] scaled_sum
     0.68%  hotspot-O2  hotspot-O2                [.] fill_grid
     0.01%  hotspot-O2  ld-linux-x86-64.so.2.37   [.] 0x0000000000022c70
```

Lines from libraries such as `ld-linux` and from the kernel (marked `[k]`) are tiny here,
so you can ignore them.

For an interactive view you can scroll through, leave off `--stdio` and everything after
it; press **q** to quit.

`column_sum` is the hot spot. Open [`hotspot.c`](samples/hotspot.c) and compare it with
`scaled_sum`: `scaled_sum` even does a division for every value, yet it's much faster.
Before reading on, take a guess at why.

## 5. Change one thing and measure again

C stores a 2D array **row by row**: `grid[0][0]`, `grid[0][1]`, `grid[0][2]`, and so on.
`scaled_sum` reads it in that order. `column_sum` reads down a column, so each value it
reads is 32 KiB away from the last one.

Memory moves to the CPU in 64-byte **cache lines** (eight `double`s). Reading in row order
uses all eight values from each line. Reading down a column uses one value, and the line
is usually gone from the cache before the loop comes back for the other seven.

Edit `column_sum` so the loops run in row order, the same way as `scaled_sum`:

```bash
vim hotspot.c
```

```c
for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
        total += grid[i][j];
```

Rebuild and time it:

```bash
gcc -O2 -g -o hotspot-rows hotspot.c
sbatch time-runs.slurm ./hotspot-rows
```

Check that the totals still match the baseline. On Frontenac this one change took the
program from about 2.7 s to about 0.3 s, almost **9× faster**, far more than any compiler
flag did.

Profile the fixed version the same way (`perf record` on `./hotspot-rows`). On Frontenac,
`column_sum` dropped from 93% to 46%, level with `scaled_sum` at 48%. When the time is spread
evenly like this, there's no single hot spot left to fix in these functions, and the next
step is a different idea from the lecture, not more of the same one.

## 6. Apply it to DOOMATHON

- **Baseline:** time a full demo, not a short run. Doom can report its own timing, so use
  that number and take it more than once.
- **Flags:** try `-O2`, `-O3`, `-flto`, and profile-guided optimization (PGO), one at a
  time, checking that the demo still plays through the same way after each.
- **Profile:** find Doom's hot spots before changing any code.
- **The many-copies puzzle:** one copy alone ran at 1,607 fps, but four at once ran at
  about 1,070 fps each. Before you decide why, ask: which parts of the node do the copies
  share? How does that connect to the memory bandwidth you measured with STREAM in
  [Meeting 04](../04-stream-benchmark-on-cac/README.md#4-build-and-submit-the-stream-benchmark)?
  Measure rather than guess.

## Questions to explore

- Try `-O3 -march=native`. Does it help this program? Why or why not?
- Change `N` to `1024` (8 MiB, much closer to the size of the cache) and repeat steps 2–5.
  Does the gap between the two loop orders change?
- In `scaled_sum`, compute `1.0 / scale` once before the loops and multiply instead of
  dividing. Is it faster? Do the totals still match? Try a scale such as `0.3`
  (`./hotspot-O2 10 0.3`).

## Clean up

From `~/qhpc/05` on the CAC, remove the builds and outputs once you're done (this keeps
`hotspot.c` and `time-runs.slurm`):

```bash
rm -f hotspot-O0 hotspot-O2 hotspot-O3 hotspot-rows perf.data perf.data.old \
  time-runs-*.out perf-record-*.out
```

## Resources

- [GCC optimize options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html): what `-O2`, `-O3`, `-flto`, and `-fprofile-use` turn on.
- [perf wiki tutorial](https://perfwiki.github.io/main/tutorial/): `perf record` and `perf report`, with examples.
- [perf-record](https://man7.org/linux/man-pages/man1/perf-record.1.html) and [perf-report](https://man7.org/linux/man-pages/man1/perf-report.1.html) manual pages.
- [sbatch reference](https://slurm.schedmd.com/sbatch.html): job options, including `--wrap`.
- [Techniques for Improving Performance](https://centers.hpc.mil/users/docs/advancedTopics/Improving_Performance.html) (DoD HPC Centers): a broad checklist covering arithmetic, memory access, vectorization, and MPI.
- [Optimizing C Code for HPC](https://www.paulnorvig.com/guides/optimizing-c-code-for-hpc.html) (Paul Norvig): flags, profilers, SIMD, and memory layout, with short C examples.
- [Optimize performance on a SLURM cluster](https://stackoverflow.com/questions/67252250/optimize-performance-on-a-slurm-cluster) (Stack Overflow): matching Slurm resource requests to the program.
- Further reading, for those who want research-level depth: [Adaptive Optimization Techniques for High-Performance Computing](https://etda.libraries.psu.edu/catalog/23713gxg5138) (Akbulut, Penn State PhD thesis, 2024) and [Competitive analysis of HPC co-scheduling strategies](https://www.sciencedirect.com/science/article/pii/S187775032600133X) (Kuchumov et al., 2026), which studies running several jobs on shared hardware at once.
