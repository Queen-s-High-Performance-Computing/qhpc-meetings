# Meeting 03: Linux, VMs and Containers

## Slide Content

We have delivered slide content thus far (check onQ for slides if you were not present). Now its time to explore on your own. 

## Now, what do you want to learn?

You can explore Linux, package an application in a container, or build a small virtual cluster on your own computer. Choose **one** question that interests you and work toward something you can explain to someone else.

You may work independently or pair up with someone exploring the same topic. Use the documentation as a starting point and decide your own next steps.

If you do not know where to start, ask us. If these options will not teach you anything new, propose a harder challenge. A working experiment, an explained error, or a justified setup plan all count as progress. You do not need to install every tool or finish an installation to learn something useful.

## Choose a topic

| Activity | A good starting point if… |
| --- | --- |
| [Terminal basics](#get-comfortable-in-a-terminal) | You are new to the command line |
| [Linux on Windows with WSL](#explore-linux-on-windows-with-wsl) | You use Windows and want a Linux environment |
| [Linux in a virtual machine](#run-linux-in-a-virtual-machine) | You want to explore a complete guest operating system |
| [Text editors: Vim and nano](#text-editors-vim-and-nano) | You want to practise editing files inside a terminal |
| [Run and inspect a container](#run-and-inspect-a-container) | You know basic terminal commands |
| [A local Kubernetes cluster](#build-a-local-kubernetes-cluster) | You understand containers and have a working runtime |
| [Automate with Ansible](#automate-a-small-task-with-ansible) | You are comfortable in a shell and have Python available |
| [Investigate dual booting](#investigate-dual-booting) | You want to research Linux running directly on your computer |
| [Design a Proxmox lab](#design-a-small-proxmox-lab) | You are interested in servers and virtualization |
| [Your own challenge](#propose-your-own-challenge) | You want to go beyond this menu |

The challenges describe outcomes. Choose whichever documentation or experiments help you answer your question. Optional [Kubernetes](#optional-kubernetes-starter), [MPI on Kubernetes](#optional-mpi-on-kubernetes-sample), and [Ansible](#optional-ansible-starter) examples are available further down if you want a small starting point.

## A few terms to keep handy

| Term | Meaning |
| --- | --- |
| Terminal / shell / CLI | The terminal is the app you type into. The shell interprets commands. A command-line interface (CLI) lets you interact with a program through text. |
| Linux / distribution | Linux is the kernel that manages hardware and running programs. A distribution, such as Ubuntu, combines it with tools and other software. macOS has a Unix command line but is not Linux. |
| Virtual machine (VM) | A guest operating system with its own kernel and virtual hardware, running on a host machine. |
| Image / container | An image packages application files and dependencies. A container is an instance created from an image. Linux containers share their Linux host's kernel; on macOS and Windows that host is usually a VM. |
| Kubernetes (K8s) / kind / kubectl | Kubernetes manages containerized workloads. kind runs local Kubernetes nodes as containers. kubectl is the command-line client used to interact with a cluster. |
| Ansible | A tool for automating configuration tasks on machines. An inventory identifies the targets; a playbook describes tasks, which use modules to do work. |
| Proxmox VE | A server virtualization platform for managing VMs and LXC system containers. LXC system containers differ from the application-container workflow introduced with Docker. |

## Activities

### Get comfortable in a terminal

**Good fit:** New CLI users on macOS, Linux, or an existing WSL installation.

**Figure out:** How can you find your current directory, navigate elsewhere, create a practice directory, and copy or rename a file without using a file manager?

**Possible outcome:** Demonstrate your workflow and explain the difference between an absolute and a relative path.

**Extension:** Search text in a file or connect two commands with a pipe.

**Starting resources:** [Ubuntu command-line introduction](https://ubuntu.com/desktop/docs/en/latest/tutorial/the-linux-command-line-for-beginners/), [Apple Terminal guide](https://support.apple.com/guide/terminal/welcome/mac), [Linux command-line cheatsheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/).

### Explore Linux on Windows with WSL

**Good fit:** Windows users who want a Linux environment through Windows Subsystem for Linux (WSL); installation may require administrator access and a restart.

**Figure out:** How do you install a distribution through WSL, open its shell, and distinguish your Linux environment from PowerShell?

**Possible outcome:** Open a Linux shell and identify the distribution and its home directory, or document the setup requirement preventing progress.

**Extension:** Investigate how Windows and Linux files are accessed from each environment.

**Starting resources:** [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install), [What is WSL?](https://learn.microsoft.com/en-us/windows/wsl/about).

### Run Linux in a virtual machine

**Good fit:** Students who want a complete guest OS and have room for an OS download and virtual disk.

**Figure out:** What CPU architecture, memory allocation, disk space, and VM software does your machine require?

**Possible outcome:** Boot a compatible Linux VM, or produce a justified setup plan if downloading takes too long. Identify the host and guest operating systems.

**Extension:** Investigate snapshots or how the guest reaches the network.

**Starting resources:** [UTM documentation for macOS](https://docs.getutm.app/), [UTM Ubuntu example](https://docs.getutm.app/guides/ubuntu/). The Ubuntu example is version-specific; check current image and architecture compatibility before following it.

### Text editors: Vim and nano

**Good fit:** Students who want to edit files in a terminal and can run Vim on macOS, Linux or WSL. Your Vim installation needs to include `vimtutor` and its lesson files.

**Figure out:** How does Vim distinguish commands from typing? How can you move through a file, insert and delete text, undo a change, save your work, and quit?

**Starting point:** Run this in your terminal's shell, rather than inside Vim:

```sh
vimtutor
```

The tutor opens a practice copy of its lesson so you can edit it as you learn. Work through as much as helps you answer your question. If the command is unavailable, check whether your Vim installation includes the tutor files.

**Possible outcome:** Edit a short practice file and explain Normal versus Insert mode. Demonstrate saving and quitting, then quitting without saving.

**Extension:** Try searching, moving by words, or repeating an edit. Compare the same editing task in `nano` and Vim.

**Starting resources:** [Vim user manual: using vimtutor](https://vimhelp.org/usr_01.txt.html#vimtutor), [Vim's first steps](https://vimhelp.org/usr_02.txt.html), [GNU nano manual](https://www.nano-editor.org/dist/latest/nano.html).

### Run and inspect a container

**Good fit:** Students comfortable with basic CLI use; installing the runtime may take much of the session.

**Figure out:** How do you run a container, list it, inspect its output, and stop it? How is an image different from a container?

**Possible outcome:** Run a small example and explain which parts came from the image.

**Extension:** Investigate port mapping or persistent data with a volume.

**Starting resources:** [Docker Desktop setup](https://docs.docker.com/desktop/), [Docker getting started](https://docs.docker.com/get-started/).

### Build a local Kubernetes cluster

A local cluster lets you explore deployment and recovery without renting cloud machines. Its nodes still share your laptop’s hardware and failure risk. Kubernetes service orchestration differs from HPC batch scheduling with tools such as Slurm.

**Good fit:** Students who already have a working container runtime and understand basic containers.

**Figure out:** How can kind create a local cluster, and how does kubectl interact with it?

**Possible outcome:** Create a cluster, inspect its node, and deploy a small application. Explain the difference between its Deployment and Pods.

**Extension:** Scale the Deployment, remove one of its Pods, and observe what happens. Alternatively, explore a multi-node kind configuration.

**Starting resources:** [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/), [Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/index.html).

### Automate a small task with Ansible

Look for **idempotence**: rerunning a task should leave an already-correct system unchanged. This depends on the module and how you use it.

**Good fit:** Students comfortable in a Linux/macOS shell, with Python available; Windows users can investigate a WSL control environment.

**Figure out:** How do an inventory, playbook, and module work together?

**Possible outcome:** Use a playbook to create a practice directory or file on localhost or a disposable VM. Run it twice and explain the reported changes.

**Extension:** Apply the same configuration to two disposable targets.

**Starting resources:** [Ansible installation](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html), [Start automating with Ansible](https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_ansible.html).

### Investigate dual booting

**Good fit:** Students curious about running Linux directly on compatible hardware. Treat this as research and planning during this session.

**Figure out:** How does dual booting differ from a VM? What do partitions, the bootloader, disk encryption, and hardware support mean for your machine?

**Possible outcome:** Explain whether dual booting suits your needs and outline a machine-specific installation and backup plan. Do not repartition your main computer as an impromptu workshop exercise.

**Extension:** Compare dual booting with trying Linux from a live USB. Apple Silicon requires a separate hardware-specific investigation; generic PC installation instructions do not apply.

**Starting resource:** [Ubuntu installation guide, including installing alongside another OS](https://ubuntu.com/tutorials/install-ubuntu-desktop).

### Design a small Proxmox lab

**Good fit:** Students interested in servers and virtualization. No installation is expected unless a suitable lab machine is already available.

**Figure out:** What does Proxmox manage? How would you divide a spare server into several useful environments?

**Possible outcome:** Sketch a host with two or three VMs, including proposed memory, storage, and networking. Explain where Ansible or Kubernetes could fit.

**Extension:** Investigate what changes when you add another physical host, and what migration, backups, and high availability require.

**Starting resources:** [Proxmox VE overview](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview), [Proxmox administration guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.pdf).

### Propose your own challenge

Choose a question that stretches your existing knowledge. Examples: automate configuration across two VMs, compare a VM-based lab with kind, or investigate recovery after a workload fails.

**Possible outcome:** State a question, run a small experiment or research a design, and explain what you learned.

**Starting resources:** Reuse the [Ansible guide](https://docs.ansible.com/projects/ansible/latest/getting_started/get_started_ansible.html), [Kubernetes concepts](https://kubernetes.io/docs/concepts/), or [Proxmox guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.pdf), depending on your question.

## Optional Kubernetes starter

<details>
<summary>A small web application to inspect and change</summary>

**Prerequisites:** kind and kubectl installed, a supported container runtime running, and internet access to download images. Use the [kind quick start](https://kind.sigs.k8s.io/docs/user/quick-start/) for setup. Run these commands in a terminal on that machine. This creates a disposable local cluster named `qhpc-m03`; use that name only if it is not already one of your clusters (`kind get clusters`).

A **Deployment** manages replicas of an application. A **Pod** groups one or more containers. Here, each application Pod runs an NGINX web server.

```sh
kind create cluster --name qhpc-m03 --wait 120s
kubectl --context kind-qhpc-m03 create deployment web --image=nginx:alpine
kubectl --context kind-qhpc-m03 rollout status deployment/web --timeout=120s
kubectl --context kind-qhpc-m03 get deployments,pods
```

The `--context` option selects this local cluster explicitly. If cluster creation or rollout fails, investigate the error before continuing. For a Pod that does not start, use `kubectl --context kind-qhpc-m03 describe pods` to inspect events.

Once the app is ready, forward a port from your computer to it:

```sh
kubectl --context kind-qhpc-m03 port-forward deployment/web 8080:80
```

Keep that command running and open [localhost:8080](http://localhost:8080). Press **Ctrl+C** to stop forwarding. If port 8080 is occupied, choose another local port. This forwards to a selected Pod and does not create a Kubernetes Service.

**Pick something to investigate:**

- How can you change the Deployment to keep two replicas running?
- What happens if you delete one of its Pods? Compare the Pod names before and after.
- What is a Service, and how does it give access to a set of Pods?
- What changes when you delete the Deployment rather than a Pod?

When finished, this removes the example cluster and everything inside it:

```sh
kind delete cluster --name qhpc-m03
```

References: [Creating a Deployment](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/), [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/).

</details>

## Optional MPI on Kubernetes sample

The [MPI sample files](samples/kubernetes-mpi/) connect the local-cluster idea to a small parallel program. This is an optional next step after the web application example, rather than a prerequisite for exploring Kubernetes.

**The intuition:** Kubernetes decides where containers run. MPI lets a program's processes communicate. An **MPI operator** teaches Kubernetes about an `MPIJob`: it prepares worker Pods, authentication and a hostfile, then starts a launcher that runs `mpirun`. Kubernetes alone does not turn ordinary code into parallel code.

| File | What it does |
| --- | --- |
| [kind.yaml](samples/kubernetes-mpi/kind.yaml) | Creates one control-plane node and two worker nodes on your computer |
| [mpi_hello.c](samples/kubernetes-mpi/mpi_hello.c) | Prints each rank's hostname, then uses `MPI_Reduce` to sum the ranks' contributions |
| [Dockerfile](samples/kubernetes-mpi/Dockerfile) | Builds the MPI program and packages Open MPI with SSH support |
| [mpi-job.yaml](samples/kubernetes-mpi/mpi-job.yaml) | Requests one launcher and two workers, with one MPI rank per worker |
| [ssh_config](samples/kubernetes-mpi/ssh_config) / [sshd_config](samples/kubernetes-mpi/sshd_config) | Allow the operator's generated keys to connect the launcher to the workers |

Each MPI worker is a **Pod**, placed on a different kind worker **node** by the manifest's anti-affinity rule. Each node is itself a container. The two ranks exchange messages through MPI, and rank 0 prints their combined result. All of these layers still share one computer's CPU and RAM; extra logical nodes do not add hardware or guarantee faster computation.

**Prerequisites:** Docker running in Linux-container mode, kind, kubectl, Git, internet access, and enough spare CPU/RAM for three local nodes and the operator. Docker builds the image for your machine's architecture, including ARM64 on Apple Silicon. On Windows, use a WSL shell with Docker integration. This sample uses the standalone [MPI Operator v0.8.2](https://github.com/kubeflow/mpi-operator/tree/v0.8.2); a full Kubeflow installation is not needed.

The MPIJob manifest has been checked against the pinned operator's schema. The Docker image and cluster workflow have not yet been built or run here. Treat the steps as an experiment and inspect errors before continuing.

### Try the MPI program before adding Kubernetes

From the repository root:

```sh
cd 03-linux-vms-and-containers/samples/kubernetes-mpi

docker build -t qhpc-mpi-hello:meeting03 .
docker run --rm qhpc-mpi-hello:meeting03 \
  mpirun -n 2 --bind-to none /home/mpiuser/mpi_hello
```

Expect two rank lines, possibly in either order, and `Sum of rank contributions: 3 (expected 3)`. This first run uses one container; it is a way to separate MPI/application problems from Kubernetes problems. The container needs at least two CPU slots for this command.

### Run across Kubernetes worker Pods

Continue from the sample directory. `qhpc-m03-mpi` is a separate disposable cluster; check `kind get clusters` and choose another name if it already exists. If you change the name, update every cluster name and `--context` below to match.

```sh
kind create cluster --name qhpc-m03-mpi --config kind.yaml --wait 180s
kind load docker-image qhpc-mpi-hello:meeting03 --name qhpc-m03-mpi
kubectl --context kind-qhpc-m03-mpi get nodes
```

Loading the image makes it available to all kind nodes without publishing it to a registry. The manifest uses `imagePullPolicy: Never` so a missing local image produces an explicit error.

Install the operator into this example cluster and wait for it:

```sh
kubectl --context kind-qhpc-m03-mpi apply --server-side -f \
  https://raw.githubusercontent.com/kubeflow/mpi-operator/v0.8.2/deploy/v2beta1/mpi-operator.yaml
kubectl --context kind-qhpc-m03-mpi wait --for=condition=Established \
  crd/mpijobs.kubeflow.org --timeout=120s
kubectl --context kind-qhpc-m03-mpi -n mpi-operator rollout status \
  deployment/mpi-operator --timeout=180s
```

Now create the namespace and job, then inspect placement and output:

```sh
kubectl --context kind-qhpc-m03-mpi apply -f mpi-job.yaml
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi wait \
  --for=condition=Succeeded mpijob/mpi-hello --timeout=180s
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi get pods -o wide
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi logs \
  -l training.kubeflow.org/job-name=mpi-hello,training.kubeflow.org/job-role=launcher \
  -c mpi-launcher --tail=-1
```

Expect rank hostnames corresponding to the two worker Pods and the same sum of `3`. The launcher orchestrates the run; it does not contribute a third rank. The operator supplies MPI's hostfile and SSH keys. The workers run SSH on port 2222 inside the cluster; no host port is published. Containers run as the unprivileged `mpiuser`. SSH host-key checks are relaxed for these disposable Pods, following the upstream example; use a reviewed configuration for a persistent/shared environment.

The worker CPU request `500m` means `0.5` CPU for scheduling; its limit of `1` caps CPU time. Neither value assigns a dedicated physical core. `slotsPerWorker: 1` tells MPI how many ranks to place on each worker, which is a separate setting from Kubernetes resource requests.

**If a step fails:**

- `ErrImageNeverPull`: confirm the image tag matches and repeat `kind load docker-image` after a rebuild.
- `Pending`: inspect `kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi describe pods`. Two worker nodes with the configured labels are required by the anti-affinity rule; also check resource requests.
- A wait timeout does not explain the cause. Inspect the Pods, job and events before retrying:

```sh
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi describe mpijob mpi-hello
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi get events --sort-by=.metadata.creationTimestamp
```

To rerun after a manifest or image change, delete the completed job, rebuild/reload the image if needed, then apply the manifest again:

```sh
kubectl --context kind-qhpc-m03-mpi -n qhpc-mpi delete mpijob mpi-hello
kubectl --context kind-qhpc-m03-mpi apply -f mpi-job.yaml
```

**Questions to investigate:** Where are the worker Pods scheduled? Why are MPI ranks different from Kubernetes nodes and vCPUs? What changes if you remove anti-affinity? Why would requesting a third worker leave a Pod Pending with only two eligible nodes? How could you change the C program to divide a numerical calculation between ranks?

When finished, delete this example cluster and everything inside it:

```sh
kind delete cluster --name qhpc-m03-mpi
```

References: [kind multi-node clusters and image loading](https://kind.sigs.k8s.io/docs/user/quick-start/), [MPI Operator's non-root example](https://github.com/kubeflow/mpi-operator/tree/v0.8.2/examples/v2beta1/pi), [Open MPI launching guide](https://docs.open-mpi.org/en/main/launching-apps/quickstart.html), [Kubernetes resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## Optional Ansible starter

<details>
<summary>A playbook you can run twice and compare</summary>

**Prerequisites:** Ansible installed in a Linux, macOS or WSL environment. Use the [installation guide](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html). This example runs on your own machine as your current user and requires no administrator privileges or remote server.

In a new practice directory of your choice, save the following as `hello.yml`. YAML uses indentation to express structure, so preserve the spaces.

```yaml
---
- name: Explore repeatable configuration
  hosts: localhost
  connection: local
  gather_facts: false
  tasks:
    - name: Write a greeting beside this playbook
      ansible.builtin.copy:
        dest: "{{ playbook_dir }}/qhpc-greeting.txt"
        content: "Hello from QHPC!\n"
        mode: "0644"
```

The play targets Ansible's implicit `localhost`, which represents your own machine. `ansible.builtin.copy` is the module doing the work. `playbook_dir` is the directory containing the playbook. The task creates or updates only `qhpc-greeting.txt` there; use a fresh practice directory so this is your experiment's file.

Run these commands from the directory containing `hello.yml`:

```sh
ansible-playbook hello.yml
ansible-playbook hello.yml
```

With no changes between runs, expect the task to report a change the first time and no change the second time. That is the behavior you are investigating.

**Pick something to investigate:**

- What happens if you change the greeting in the playbook and run it again?
- What happens if you edit or delete the generated file instead?
- How would an inventory let you apply a configuration to a disposable VM?
- Why might an arbitrary shell command behave differently when repeated?

Afterwards, delete the practice files if you no longer want them.

References: [Ansible playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html), [the copy module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/copy_module.html), [implicit localhost](https://docs.ansible.com/projects/ansible/latest/inventory/implicit_localhost.html).

</details>

## Share what you discovered

In the last five minutes, be ready to explain:

- What did you try, and what did you learn?
- What worked, or what blocked you?
- What would you investigate next?

If you need help, bring the question you were trying to answer, the command or action you tried, and the relevant error. An obstacle you can explain is useful progress.

**Optional GitHub follow-up:** spot something unclear on this page and propose a small improvement. Look at how a commit records a change and how a pull request asks for it to be reviewed. You can use a personal fork if you do not have write access. [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) introduces this workflow.

The aim is to leave with a clearer mental model and one concrete next step.
