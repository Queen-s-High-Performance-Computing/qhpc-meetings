# Create an SSH key

SSH (Secure Shell) lets you securely connect to another computer and run commands. We create an SSH key pair to prove our identity when connecting. Many services use SSH keys for secure authentication.

## Prerequisites

- **macOS / Linux:** Open **Terminal**.
- **Windows:** Open **Windows Terminal** with **WSL** or [Git Bash](git-on-windows.md).
- Run `ssh -V` to check SSH is available.
- Use the **same shell** throughout; SSH keys created in WSL are not automatically shared with Windows.

## 1. Create or reuse a key

If you already have a suitable SSH key, reuse it. Otherwise, run:

**Bash (macOS / Linux / WSL / Git Bash):**

```bash
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace the email with your own (recommend that its the same email you use with GitHub). Accept the default filename, `id_ed25519`, and choose a passphrase. If a key already exists, keep it or choose another filename; do not overwrite it.

- `~/.ssh/id_ed25519`: your **private key**, which stays on your computer.
- `~/.ssh/id_ed25519.pub`: your **public key**, which you register with services.

If you choose another key filename, adjust later paths.

## 2. Strongly Recommended: add the public key to GitHub

This lets you authenticate Git operations over SSH. Display the public key:

**Bash (macOS / Linux / WSL / Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire line. In GitHub, open **Settings → SSH and GPG keys → New SSH key**. Give it a descriptive title, select **Authentication Key**, paste the public key, and save.

For CAC access, continue with [Meeting 04](../04-stream-benchmark-on-cac/README.md#1-configure-ssh-to-the-cac), which registers the public key separately.

## Resources

- [Git for Windows](https://gitforwindows.org/): includes Git Bash.
- [OpenSSH key generation](https://man.openbsd.org/ssh-keygen).
- [GitHub: generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
- [GitHub: add a public key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
