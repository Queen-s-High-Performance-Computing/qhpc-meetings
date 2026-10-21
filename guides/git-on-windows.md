# Install Git and Git Bash on Windows

Git for Windows includes **Git Bash**, which lets you follow the same Bash examples as members using macOS, Linux, or WSL. Bash is generally an easier to use CLI for terminal than Windows Powershell and Batch.

## Prerequisites

- Windows 10 or 11.
- [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install) (usually pre-installed) if you want Git Bash as a terminal tab.

## Install

1. Download and run the installer from [Git for Windows](https://gitforwindows.org/).
2. On **Select Components**, enable **Add a Git Bash Profile to Windows Terminal**.
3. Keep the other defaults unless you have a preference, then finish installation.

## Open Git Bash

Reopen **Windows Terminal**, open the dropdown beside the **+** button, and choose **Git Bash**. You can also open **Git Bash** from the Start menu.

If the profile is missing, open **Settings → Add a new profile → New empty profile**. Name it **Git Bash** and set **Command line** to the following, adjusting the path if needed, then save:

```text
"C:\Program Files\Git\bin\bash.exe" --login -i
```

In the Git Bash tab, check:

```bash
git --version
bash --version
ssh -V
```

Each command should print a version. You can now follow blocks labelled **Bash (macOS / Linux / WSL / Git Bash)**, starting with the [SSH-key guide](ssh-keys.md).

## Resources

- [Git for Windows](https://gitforwindows.org/) and [FAQ](https://gitforwindows.org/faq).
- [Windows Terminal installation](https://learn.microsoft.com/en-us/windows/terminal/install) and [profile settings](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/profile-general).
