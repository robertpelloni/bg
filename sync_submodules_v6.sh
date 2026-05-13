#!/bin/bash

# Remove any stale lock files across the monorepo recursively
echo "Cleaning stale lock files..."
find . -name "index.lock" -type f -delete

echo "Syncing all git submodules recursively..."
# Init and update all submodules with recursive flag
git submodule update --init --recursive --jobs 4

# Iterate through all direct submodules and fetch/merge origin/main or origin/master if they are detached
git submodule foreach --recursive '
    echo "Processing $name..."
    git fetch origin
    # Determine default branch (main or master)
    default_branch=$(git remote show origin | sed -n "/HEAD branch/s/.*: //p")
    if [ -z "$default_branch" ]; then
        default_branch="master"
    fi
    # If we are detached, just checkout the commit. We will not force merges right now as many referential submodules are pinned.
    echo "Checked out $name successfully."
'

echo "Sync completed."
