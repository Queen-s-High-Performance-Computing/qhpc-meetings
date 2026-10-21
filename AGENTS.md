# Agent guide

## Purpose

Write concise guides, samples, and activities for QHPC members to complete after
educational meetings. The usual workflow is slides, then workshop-style tasks.
Include enough context for newcomers. Use GitHub-readable Markdown. Asynchronous
tasks are a future option.

Read README.md, CONTRIBUTING.md, and the affected meeting or shared guide before
editing. Check `git status --short` and review staged, unstaged, and new files.
Preserve manual edits, screenshots, and existing staging; do not restage or discard
the user's work while making a targeted change.

## Layout

- `README.md`: meeting catalogue.
- `NN-topic/README.md`: meeting guide; `samples/` and `assets/` are optional.
- `guides/`: short setup guides shared between meetings.
- `templates/meeting.md`: starting point for new meetings.
- `scripts/check_repo.py`: offline structure and local file-link checks.

## Rules

- Keep materials concise and to the point. Use short steps and small examples.
- Choose a tutorial, task, sample, or open-ended challenge to suit the meeting.
- Link website documentation at least once for each technical tool introduced.
  Collect documentation and useful videos in a **Resources** section. Prefer
  official documentation and check current technical claims against it.
- Put required knowledge, access, tools, and preparatory reading in a
  **Prerequisites** section before the guide or task. Omit it when unnecessary.
- Reuse setup guides in `guides/` instead of duplicating them. Link required guides
  from prerequisites and add new shared guides to the root README's setup links.
- Distinguish local commands from CAC commands. State working directories,
  expected results, and cleanup where needed. Do not invent cluster settings.
- Name the app/shell to open and show a short availability check for required tools.
  Use clear placeholders and preserve existing learner files and configuration.
- Use Bash for all shell commands and `bash` code blocks on every platform.
  Windows members must install Git for Windows and use the Git Bash profile in
  Windows Terminal. Note platform-specific tool features where relevant.
  Label shared examples **Bash (macOS / Linux / WSL / Git Bash)** so Windows members
  can recognize their Bash option alongside the others.
  After SSH login, CAC commands use the remote Linux shell on every platform.
  Keep Bash examples compatible with macOS's bundled Bash unless a newer version
  is listed as a prerequisite. Shared syntax does not imply shared tool features.
- Agents can draft and check files locally; team members handle CAC execution.
  No verification labels, run logs, or recurring sample reviews are required.
  Never claim a run that did not happen. Run examples only within the task's scope.
- Use permanent zero-padded decimal meeting IDs (`03`, `04`, `10`). Confirm new
  topics/IDs from the task, use the template, and update the root catalogue.
- One approval from Anthony Botticchio, Lucas Yaskowich, or Charlie Bolt is
  sufficient to merge. Do not merge, publish, or push without task authorization.
- Keep essential context available without private slides. Link external material
  and preserve attribution. Give screenshots alt text and supporting text steps;
  keep private keys, passwords, and tokens out of examples and assets. Licensing
  remains undecided.
- Keep CONTRIBUTING.md, this guide, and the meeting template consistent when
  changing authoring conventions.

## Checks and handoff

```bash
python3 scripts/check_repo.py
git diff --check
git diff --cached --check
```

Run from the repository root with Python 3.9 or newer; see CONTRIBUTING.md if Python
has a different command name. Inspect untracked files directly: Git diff checks omit them.
Review the Markdown layout. The checker does not validate heading anchors,
external URLs, rendering, or sample behavior. Report checks and execution limits
briefly, including platforms or CAC steps that were not run.
