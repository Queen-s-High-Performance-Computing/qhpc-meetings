# QHPC Meetings

Guides, samples, tasks, and quick activities to supplement QHPC educational meetings. We generally prepare slides, then use this repository for workshop-style follow-on activities that members can work through on their own or with others.

Use this repository during meetings or return to it afterwards to keep learning. You can read the guides and follow their links directly on GitHub.

The resources are written for attendees, with enough context for newcomers. You do not need access to meeting slides to begin exploring the activities.

## Table of contents

| Meeting | Topic | What you can explore |
| --- | --- | --- |
| 03 | [Linux, VMs and Containers](03-linux-vms-and-containers/README.md) | Terminal basics, Linux environments, containers, local Kubernetes clusters, Ansible, and Proxmox labs |
| 04 | [SSH and Slurm on the CAC](04-ssh-and-slurm/README.md) | Configure SSH, edit a job script with Vim, submit it, and inspect its output |

## Getting started

Open a meeting above and choose an activity that interests you. Each guide includes starting resources and possible outcomes, with options for different experience levels.

Setup guides: [Git and Git Bash on Windows](guides/git-on-windows.md) · [Create an SSH key](guides/ssh-keys.md).

Some activities use the CAC cluster available to the team; those guides describe the access and tools you need. The repository may also support asynchronous tasks in future.

Found an unclear explanation or a useful resource? Open an issue or propose an improvement through a pull request.

## Developing resources

Read [CONTRIBUTING.md](CONTRIBUTING.md) for content conventions, validation, and design references. Start a new meeting from [the template](templates/meeting.md). AI agents should also read [AGENTS.md](AGENTS.md).

Folders use permanent decimal meeting IDs (`03-topic`, `10-topic`) so they sort on GitHub. Keep an existing meeting's ID when updating it; gaps are expected when a meeting has no resources here.

From the repository root, check structure and local file links with Python 3.9 or newer:

```sh
python3 scripts/check_repo.py
git diff --check
```

These checks also run in GitHub Actions. They check repository structure and links; team members with access handle CAC execution when needed. Contribution review is the responsibility of Anthony Botticchio, Lucas Yaskowich, and Charlie Bolt; see [reviewer access status](CONTRIBUTING.md#reviewers).
