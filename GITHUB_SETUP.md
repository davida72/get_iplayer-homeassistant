# GitHub Setup Guide

This guide will help you publish your Home Assistant addon to GitHub so others can use it.

## Step 1: Initialize Git Repository

```bash
cd /Users/davidamor/GitHub/get_iplayer-homeassistant
git init
git add .
git commit -m "Initial commit: get_iplayer Home Assistant addon"
```

## Step 2: Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `get_iplayer-homeassistant`
3. Description: "Home Assistant addon for downloading BBC iPlayer content using get_iplayer"
4. Make it **Public** (so others can add it to their Home Assistant)
5. **Do NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

## Step 3: Push to GitHub

```bash
git remote add origin https://github.com/davida72/get_iplayer-homeassistant.git
git branch -M main
git push -u origin main
```

If you're using SSH instead of HTTPS:

```bash
git remote add origin git@github.com:davida72/get_iplayer-homeassistant.git
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages (Optional)

To create a nice landing page:

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Under "Source", select **main** branch
4. Click **Save**

## Step 5: Test the Addon

Before sharing with others, test it yourself:

1. In Home Assistant, go to **Settings** → **Add-ons** → **Add-on Store**
2. Click the **three dots** (⋮) in the top right
3. Select **Repositories**
4. Add: `https://github.com/davida72/get_iplayer-homeassistant`
5. Refresh the page
6. Find "get_iplayer Downloader" and install it
7. Configure it with your desired settings
8. Start the addon and check the logs

## Step 6: Share with Others

Once tested, you can share your addon:

1. Add the repository URL to your Home Assistant: `https://github.com/davida72/get_iplayer-homeassistant`
2. Share the URL on Home Assistant forums or communities
3. Add a badge to your README (optional):

```markdown
[![Add to Home Assistant](https://img.shields.io/badge/Add%20to-Home%20Assistant-blue)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fdavida72%2Fget_iplayer-homeassistant)
```

## Updating the Addon

When you make changes:

1. Update the version number in `get-iplayer-downloader/config.yaml`
2. Update `get-iplayer-downloader/CHANGELOG.md` with changes
3. Commit and push:

```bash
git add .
git commit -m "Version X.Y.Z: Description of changes"
git push
```

Users will see the update in their Home Assistant addon store.

## Repository Structure

Your repository should look like this:

```
get_iplayer-homeassistant/
├── .gitignore
├── README.md
├── repository.json
├── GITHUB_SETUP.md
└── get-iplayer-downloader/
    ├── CHANGELOG.md
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── build.yaml
    ├── config.yaml
    └── run.py
```

## Troubleshooting

### Authentication Issues

If you have trouble pushing to GitHub:

1. Make sure you're authenticated with GitHub CLI or SSH
2. Or use a Personal Access Token instead of password:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with `repo` scope
   - Use this token as your password when prompted

### Addon Not Showing in Home Assistant

1. Make sure the repository is public
2. Check that `repository.json` exists in the root
3. Verify the URL is correct
4. Try removing and re-adding the repository in Home Assistant

## Additional Resources

- [Home Assistant Add-on Documentation](https://developers.home-assistant.io/docs/add-ons)
- [get_iplayer Documentation](https://github.com/get-iplayer/get_iplayer/wiki)
- [Home Assistant Community Forum](https://community.home-assistant.io/)
