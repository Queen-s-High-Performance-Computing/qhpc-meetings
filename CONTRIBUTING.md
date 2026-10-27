# Contributing

Prepare members with short prerequisite reading and provide activities for use
during or after meetings. Keep contributions focused and concise, with enough
context for newcomers who do not have the slides.

This file owns the content standards. [AGENTS.md](AGENTS.md) adds agent workflow
instructions.

## Reviewers

**One approval** from Anthony Botticchio, Lucas Yaskowich, or Charlie Bolt is
sufficient to merge.

## Layout

- `README.md`: meeting catalogue and **Available guides** table.
- `NN-topic/README.md`: meeting instructions, with optional `samples/` and `assets/`.
- `guides/`: short shared reading and setup guides.
- `guides/resources/`: images, PDFs, and other shared-guide assets.
- `templates/meeting.md`: starting point for new meetings.
- `scripts/check_repo.py`: offline structure and local file-link checks.

## Add a meeting

Use `NN-topic-in-kebab-case`, such as `04-stream-benchmark-on-cac`. IDs are permanent,
zero-padded decimal numbers; keep existing IDs and allow gaps. The current format
supports `01` through `99`.

1. Confirm the topic and unused ID from the task or with a maintainer.
2. Copy [the template](templates/meeting.md) to `NN-topic/README.md` and fill it in.
3. Add `samples/`, `assets/`, or `instructor-notes.md` only when useful.
4. Add the meeting to the root [catalogue](README.md#meetings).

## Shared guides

Keep `guides/` short and focused on reading: brief explanations, compact command
tables, and small examples. Put extended practice in separate activity directories.
Reuse shared guides rather than repeating setup instructions in meetings.

Guides should usually be linked from meeting **Prerequisites**. Add each guide to
the root [Available guides](README.md#available-guides) table.

## Write a guide or task

- Include only information students need for the stated goal.
- Use short tutorials, tasks, samples, or exploration questions as appropriate.
- Name the app/shell to open. For required tools, give a quick availability check
  and a setup link if missing. Use clear placeholders for learner-specific values.
  Name the terminal app/profile without adding a separate `bash` startup command.
- Put **Prerequisites** before the main content, using short bullet lists for
  required tools, access, knowledge, and reading. List required guides by linked
  title; add setup details only when necessary.
- In meetings, group prerequisites under **Software and access** and
  **Core skills and guides**, omitting empty groups. Keep requirements for optional
  activities beside those activities and optional further reading in **Resources**.
  Do not require mastery of what the meeting teaches.
- Every meeting involving Linux must list
  `- [Using the Linux CLI](../guides/using-the-linux-cli.md)` as prerequisite reading.
- Link website documentation at least once for each technical tool introduced.
  Collect technical documentation and useful videos in a **Resources** section.
  Prefer official documentation; check version-sensitive claims before adding them.
- For YouTube links, prefer a clickable Markdown thumbnail alongside the video
  title and creator. Use `[![Description](THUMBNAIL_URL)](VIDEO_URL)` with
  descriptive alt text.
- State where commands run, what they change, and the expected result. Include
  cleanup where needed. Preserve existing learner files and configuration.
- Use Bash for all shell commands and `bash` code blocks on every platform.
  On Windows, simply say to open Windows Terminal with WSL or Git Bash.
  Link the [Windows setup guide](guides/git-on-windows.md) when Git Bash setup is needed.
  Label shared examples **Bash (macOS / Linux / WSL / Git Bash)**.
  Keep Bash examples compatible with macOS's bundled Bash unless a newer version
  is a stated prerequisite. Check tool/client features separately from shell syntax.
- After SSH login, CAC commands use the remote Linux shell on every platform.
- Prefer linking external material and preserve attribution. Include local PDFs,
  PDF previews, or other graphics when requested by the user.
- Keep meeting assets beside their meeting guide and shared-guide assets in
  `guides/resources/`. Use descriptive filenames, relative links, and image alt text;
  accompany screenshots with text instructions.
- Keep private keys, passwords, and tokens out of examples and assets.
- When renaming files or headings, update incoming links, including heading anchors.

## CAC examples

Use supplied or documented cluster settings and mark account-specific values
clearly. Do not invent cluster settings; team members with CAC access handle
cluster execution.

Verification labels, execution records, and recurring sample reviews are not
required. Describe checks honestly; do not imply a CAC run when only local checks
were possible. Repository licensing remains undecided.

## Check and submit

From the repository root, with Git and Python 3.9 or newer; no extra Python packages
are needed.

**Bash (macOS / Linux / WSL / Git Bash):**

```bash
python3 scripts/check_repo.py
git diff --check
git diff --cached --check
```

In Windows Git Bash, use `py -3` or `python` in place of `python3` if needed. Review
staged and unstaged changes, plus untracked files directly; Git diff checks omit
untracked files.

The script checks meeting names, IDs, titles, catalogue coverage, and file targets
in inline Markdown links. It skips code examples and does not check anchors,
reference-style/HTML links, web URLs, rendering, or sample execution. Review the
affected Markdown, including anchors and image links. Report checks and execution
limits briefly; local Bash checks do not establish Windows or CAC behavior. GitHub
Actions runs repository checks; required checks and approvals need repository settings.

Keep the [meeting template](templates/meeting.md) aligned with these standards.
Keep agent workflow instructions in AGENTS.md and preserve existing edits and staging.

## Resources

Setup and design references:

- [Python on Windows](https://docs.python.org/3/using/windows.html): Python and launcher setup for repository checks.
- [Carpentries episode structure](https://carpentries.github.io/sandpaper-docs/episodes.html): objectives, challenges, and instructor notes.
- [HPC Carpentry](https://github.com/carpentries-incubator/hpc-intro): learner resources and contribution guidance.
- [Yale Intro to HPC](https://github.com/ycrc/Intro-to-HPC): workshop examples alongside teaching material.
