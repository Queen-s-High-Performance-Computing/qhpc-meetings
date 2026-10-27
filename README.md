# QHPC Meetings

Short guides for prerequisite reading, plus samples, tasks, and activities for QHPC educational meetings. We generally prepare slides, then use this repository for workshop-style activities that members can work through on their own or with others.

Use this repository during meetings or return to it afterwards to keep learning. You can read the guides and follow their links directly on GitHub.

The resources are written for attendees, with enough context for newcomers. You do not need access to meeting slides to begin exploring the activities.

## Meetings

| Meeting | Topic | What you can explore |
| --- | --- | --- |
| 03 | [Linux, VMs and Containers](03-linux-vms-and-containers/README.md) | Terminal basics, Linux environments, containers, local Kubernetes clusters, Ansible, and Proxmox labs |
| 04 | [STREAM Benchmark on the CAC](04-stream-benchmark-on-cac/README.md) | Configure SSH, submit a job script with Vim, then run the STREAM benchmark and read it with the roofline model |

## Available guides

| Topic | Description |
| --- | --- |
| [Using the Linux CLI](guides/using-the-linux-cli.md) | Basic commands, pipes, grep, and Linux cheat sheets |
| [Create an SSH key](guides/ssh-keys.md) | Create an SSH key pair and register the public key with services |
| [Git on Windows](guides/git-on-windows.md) | Install Git and open Git Bash in Windows Terminal |

## Getting started

Open a meeting above and start with its **Prerequisites**: check **Software and access**, then read the linked **Core skills and guides** and complete any required setup. Each meeting includes starting resources and possible outcomes, with options for different experience levels. Check any extra prerequisites beside the activity you choose.

All shell examples use Bash. On Windows, open **Windows Terminal** with **WSL** or **Git Bash**.

Some activities use the CAC cluster available to the team; those guides describe the access and tools you need. The repository may also support asynchronous tasks in future.

Found an unclear explanation or a useful resource? Open an issue or propose an improvement through a pull request.

## Developing resources

Read [CONTRIBUTING.md](CONTRIBUTING.md) for content conventions, validation, and design references. Start a new meeting from [the template](templates/meeting.md). AI agents should also read [AGENTS.md](AGENTS.md).

Folders use permanent decimal meeting IDs (`03-topic`, `10-topic`) so they sort on GitHub. Keep an existing meeting's ID when updating it; gaps are expected when a meeting has no resources here.

From the repository root, check structure and local file links with Python 3.9 or newer:

```bash
python3 scripts/check_repo.py
git diff --check
```

These checks also run in GitHub Actions. They check repository structure and links; team members with access handle CAC execution when needed. Contribution review is the responsibility of Anthony Botticchio, Lucas Yaskowich, and Charlie Bolt; see [reviewer access status](CONTRIBUTING.md#reviewers).
