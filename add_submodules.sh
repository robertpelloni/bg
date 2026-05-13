#!/bin/bash

# Define array of repos
repos=(
    "https://github.com/aseprite/aseprite"
    "https://github.com/tstamborski/sprite-studio-64"
    "https://github.com/stipple-effect/stipple-effect"
    "https://github.com/Pakz001/Raylib-Examples"
    "https://github.com/csprite/csprite"
    "https://github.com/RetroNick2020/raster-master"
    "https://github.com/Wiering/Tile-Studio"
    "https://github.com/counter185/voidsprite"
    "https://github.com/GuckTubeYT/GrowTools"
    "https://github.com/haroldo-ok/retro-game-editor"
    "https://github.com/jval1972/SpeedEd"
    "https://github.com/PandaDevOfficial/aseprite-guide"
    "https://github.com/Rangi42/tilemap-studio"
    "https://github.com/blurymind/tilemap-editor"
    "https://github.com/albin-johansson/tactile"
    "https://github.com/wmltogether/Simple-Sprite-Tile-2D"
    "https://github.com/Dark-Peace/bottled-up-tilemap"
    "https://github.com/MagnonGames/DTile"
    "https://github.com/Orama-Interactive/Pixelorama"
    "https://github.com/PixiEditor/PixiEditor"
    "https://github.com/LibreSprite/LibreSprite"
    "https://github.com/cloudhead/rx"
    "https://github.com/piskelapp/piskel"
    "https://github.com/JannisX11/blockbench"
    "https://github.com/CytopiaTeam/Cytopia"
    "https://github.com/guillaumechereau/goxel"
    "https://github.com/mapeditor/tiled"
    "https://github.com/Ogmo-Editor-3/OgmoEditor3-CE"
    "https://github.com/miniupnp/grafx2"
    "https://github.com/deverac/grafx2-dos"
    "https://github.com/Dakkra/PyxleOS"
)

# Loop and add each
for repo in "${repos[@]}"; do
    repo_name=$(basename -s .git "$repo")
    path="references/editors/$repo_name"

    if [ ! -d "$path" ]; then
        echo "Adding submodule: $repo at $path"
        git submodule add -f "$repo" "$path"
        # Wait a bit between adds to avoid git lock issues
        sleep 1
    else
        echo "Skipping $repo_name, directory already exists."
    fi
done
