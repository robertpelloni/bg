import re

with open("bobsgameweb/src/renderer/engine/rpg/ClientGameEngine.ts", "r") as f:
    content = f.read()

# Instead of using DemoWorld, map manager should be rendering it natively. Let's see what MapManager offers.
# Right now we'll do MapManager + Player since DemoWorld did it all. Let's check MapManager rendering setup first.
