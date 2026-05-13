#!/bin/bash
repos=(
    "https://github.com/huggingface/diffusers"
    "https://github.com/openai/shap-e"
    "https://github.com/CompVis/stable-diffusion"
    "https://github.com/lllyasviel/ControlNet"
    "https://github.com/Stability-AI/stablediffusion"
)
for repo in "${repos[@]}"; do
    repo_name=$(basename -s .git "$repo")
    path="references/ai/$repo_name"
    if [ ! -d "$path" ]; then
        echo "Adding submodule: $repo at $path"
        git submodule add -f "$repo" "$path"
        sleep 1
    else
        echo "Skipping $repo_name"
    fi
done
