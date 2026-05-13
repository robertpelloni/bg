# bgeditor Cross-Platform Port Strategy

## Goal
Port the legacy Java `bgeditor` to:
1. Native C++ using Qt6 (`bobui`).
2. Native JavaFX.
3. Web-based PixiJS tool (via `bobsgameweb`).

## C++ / Qt6 Strategy (`okgame`)
- Leverage the newly added `bobui` submodule.
- `bobui` provides a Qt6 wrapper around standard editor components (panels, timelines, property inspectors).
- We will replace the raw SDL2/SDL3 immediate-mode GUI in the `CustomGameEditor` with structured Qt6 QWidgets.
- **Action:** Ensure `CMakeLists.txt` in `okgame` includes paths to the `bobui` submodule.

## JavaFX Strategy
- The current Java editor relies on older Swing/AWT/LWJGL 2 paradigms.
- **Action:** Transition the core editor frame to `javafx.scene.Scene` while embedding the LibGDX `Lwjgl3Application` within a `JFXPanel`. This allows the game engine to render within a modern UI window.

## Web Strategy (`bobsgameweb`)
- Utilize the `CustomGameEditorScene.ts`.
- Expand UI components (using `@pixi/ui` or HTML DOM overlays) to mimic the complex panels of a native desktop application.
