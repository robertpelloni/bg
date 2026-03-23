# DEPLOY: Deployment Instructions

## 1. General Deployment Workflow
The Omni-Workspace uses a synchronized deployment strategy to ensure all platforms are updated together.

## 2. Platform-Specific Steps

### A. C++ (okgame)
1.  **Build:** Run `_build.bat` or use CMake to generate the project files.
2.  **Verify:** Ensure `steam_api64.dll` is present if building with Steamworks.
3.  **Distribute:** Run `_make distro.bat` to package the executable and assets into the `dist/` folder.

### B. Java (bobsgameonlinejava)
1.  **Build:** Run `./gradlew build` (ensure Java 21 is active).
2.  **Package:** Use `./gradlew desktop:dist` to create the runnable JAR.
3.  **Asset Sync:** Ensure `res/` folder is correctly linked or copied.

### C. Web (bobsgameweb)
1.  **Build:** Run `npm run build` in the root of `bobsgameweb`.
2.  **Server:** Restart the Node.js server in `bobsgameweb/server/`.
3.  **Deploy:** Upload the `dist/` content to the web host.

## 3. Automation Scripts
- `scripts/sync_all.sh`: Fetches and pulls all submodules.
- `scripts/deploy_all.sh`: (Planned) Triggers builds for all platforms sequentially.

## 4. Versioning
Always bump the version in the root `VERSION` file and all project-specific `VERSION.md` files before a deployment.
