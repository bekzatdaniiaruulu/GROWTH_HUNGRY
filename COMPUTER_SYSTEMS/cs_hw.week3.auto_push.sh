#!/bin/bash

# === Road to my repo ===
REPO_DIR="/Users/bekzat/Documents/computer-systems"

# sWitch to repo file
cd "$REPO_DIR" || exit

# === Add all new changes and files ===
git add .

# check if there are any changes to commit
if ! git diff --cached --quiet; then
    # create a commit with the current date and time as the message
    COMMIT_MSG="Auto update: $(date)"
    git commit -m "$COMMIT_MSG"

    # send changes to GitHub
    git push origin main

    echo "✅ Changes pushed to GitHub at $(date)"
else
    echo "No new files found."
fi

# === End of script ===
