import sys
import re

def increment_version(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    match = re.search(r"(\d+\.\d+\.)(\d+)", content)
    if match:
        prefix = match.group(1)
        build = int(match.group(2))
        new_version = f"{prefix}{build + 1}"
        new_content = content.replace(f"{prefix}{build}", new_version)
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Bumped version to {new_version} in {filepath}")
    else:
        print(f"Could not find version string in {filepath}")

increment_version("bobsgameweb/package.json")
increment_version("bobsgameweb/src/renderer/scenes/MainMenuScene.ts")
increment_version("bobsgameonlinejava/src/main/java/com/bobsgame/IndexServerMain.java")
