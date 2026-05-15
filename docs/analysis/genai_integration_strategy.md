# Generative AI Integration Strategy (Omni-Engine)

## Objective
Seamlessly integrate the newly added Generative AI submodules (`Stable Diffusion`, `Diffusers`, `Shap-E`, `ControlNet`) located in `references/ai/` into the `bgeditor` (Omni-Engine) workflow. This will allow users to generate 2D sprites, tilesets, and 3D voxel models directly from text prompts within the editor.

## Architecture

### 1. The Python AI Daemon
The Node.js Socket.io backend is not suited for heavy ML inference. Instead, we will wrap the Python-based AI models in a lightweight local FastAPI or Flask daemon (`ai_daemon.py`).
- **Input:** JSON payload containing prompt, dimensions, mode (text-to-sprite, image-to-3d), and optional ControlNet conditioning image.
- **Processing:** Utilizes the `diffusers` library pipelines and `shap-e` model wrappers.
- **Output:** Base64 encoded PNG or GLTF/OBJ model data.

### 2. Node.js Backend Proxy
The existing `bobsgameweb/server/index.js` will act as a proxy:
- Endpoint: `POST /api/generate/sprite`
- The Node server validates the user's session/token, rate-limits requests, and forwards the payload to the local Python AI Daemon running on a separate port (e.g., `8000`).

### 3. Web Editor Frontend
- In `CustomGameEditorScene.ts`, we will add a `GenerativeAIManager` UI panel.
- Users input text prompts (e.g., "A retro 16-bit fiery sword sprite").
- The UI sends the request to `/api/generate/sprite`.
- The returned image is loaded into a PixiJS `Texture` and injected directly into the Aseprite-like canvas or animation timeline.

## Next Steps
- Stand up the Express HTTP POST routes in `server/index.js`.
- Construct the `GenerativeAIPanel` UI in the web client.
