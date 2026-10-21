# Contributing

Improve a guide, report an unclear explanation, or propose a meeting activity.
Keep contributions focused and concise. [AGENTS.md](AGENTS.md) adds instructions
for agents; the content standards below apply to everyone.

## Reviewers

**One approval** from Anthony Botticchio, Lucas Yaskowich, or Charlie Bolt is
sufficient to merge.

## Add a meeting

Use `NN-topic-in-kebab-case`, such as `04-ssh-and-slurm`. IDs are permanent,
zero-padded decimal numbers; keep existing IDs and allow gaps. The current format
supports `01` through `99`.

1. Confirm the topic and unused ID from the task or with a maintainer.
2. Copy [the template](templates/meeting.md) to `NN-topic/README.md` and fill it in.
3. Add `samples/`, `assets/`, or `instructor-notes.md` only when useful.
4. Add the meeting to the root [catalogue](README.md#table-of-contents).

Put reusable setup instructions in `guides/` with descriptive filenames such as
`git-on-windows.md`. Link them from relevant prerequisites and the root README's
setup links rather than repeating installation steps in each meeting.

## Write a guide or task

We generally make slides, then provide follow-on activities for members to work
through independently. Asynchronous work may be added later.

- Stay concise. Give enough context for someone who missed the slides.
- Use short tutorials, tasks, samples, or exploration questions as appropriate.
- Name the app/shell to open. For required tools, give a quick availability check
  and a setup link if missing. Use clear placeholders for learner-specific values.
- Put required knowledge, accounts, tools, and preparatory reading in a
  **Prerequisites** section before the guide/task, when needed.
- Link website documentation at least once for each technical tool introduced.
  Collect technical documentation and useful videos in a **Resources** section.
  Prefer official documentation; check version-sensitive claims before adding them.
- State where commands run, what they change, and the expected result. Include
  cleanup where needed. Preserve existing learner files and configuration.
- Use `bash` blocks for macOS, Linux, WSL, and Windows Git Bash. Use `powershell`
  blocks compatible with Windows PowerShell 5.1 for native Windows; PowerShell 7
  (`pwsh`) is not required. Provide separate snippets where commands or paths differ.
  Label shared examples **Bash (macOS / Linux / WSL / Git Bash)**.
  Keep Bash examples compatible with macOS's bundled Bash unless a newer version
  is a stated prerequisite. Check tool/client features separately from shell syntax.
- Keep screenshots beside their guide, with descriptive alt text and supporting
  text instructions. Reuse existing asset folders and relative links; keep private
  keys, passwords, and tokens out of examples and screenshots.

## CAC examples

Agents can draft and inspect materials locally; team members with CAC access
handle cluster execution. Use supplied or documented cluster settings and mark
account-specific values clearly.

Verification labels, execution records, and recurring sample reviews are not
required. Describe checks honestly in the pull request; do not imply a CAC run
when only local checks were possible. Licensing remains undecided; preserve
attribution and link external material rather than copying it wholesale.

## Check and submit

From the repository root, with Git and Python 3.9 or newer; no extra Python packages
are needed.

**Bash (macOS / Linux / WSL / Git Bash):**

```bash
python3 scripts/check_repo.py
git diff --check
git diff --cached --check
```

On Windows Git Bash, use `py -3` in place of `python3` if needed.

**Windows PowerShell:**

```powershell
py -3 scripts/check_repo.py
git diff --check
git diff --cached --check
```

If Python is installed as `python` instead, use that command. Review staged and
unstaged changes, plus untracked files directly; Git diff checks omit untracked files.

The script checks meeting names, IDs, titles, catalogue coverage, and file targets
in inline Markdown links. It skips code examples and does not check anchors,
reference-style/HTML links, web URLs, rendering, or sample execution. Review the
affected Markdown, including anchors and image links. Report checks and execution
limits briefly; local Bash checks do not establish Windows or CAC behavior. GitHub
Actions runs repository checks; required checks and approvals need repository settings.

When changing authoring conventions, keep this file, AGENTS.md, and the meeting
template consistent. Preserve existing manual edits and staging during changes.

## Resources

Setup and design references:

- [Python on Windows](https://docs.python.org/3/using/windows.html): Python and launcher setup for repository checks.
- [Carpentries episode structure](https://carpentries.github.io/sandpaper-docs/episodes.html): objectives, challenges, and instructor notes.
- [HPC Carpentry](https://github.com/carpentries-incubator/hpc-intro): learner resources and contribution guidance.
- [Yale Intro to HPC](https://github.com/ycrc/Intro-to-HPC): workshop examples alongside teaching material.
