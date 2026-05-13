# Editor Feature Parity Analysis (okgame vs bobsgameweb)

## C++ `CustomGameEditor.cpp` (okgame)
- Uses immediate-mode rendering via raw SDL arrays.
- Features deep sequence editing (`GameSequenceEditor.cpp`).
- Supports block behavior overrides (e.g., BOMB, WEIGHT, SUBTRACTOR).

## Web `CustomGameEditorScene.ts` (bobsgameweb)
- Utilizes PixiJS v8 object-based rendering (`Container`, `Graphics`, `Text`).
- **Missing:** The deep sequence editing menus. Currently, it allows setting game properties but lacks the graphical visual scripting node layout present in the C++ version.
- **Missing:** Full property mapping for advanced block types.

## Path Forward for the Omni-Engine
- We must port the visual node layout from `GameSequenceEditor.cpp` into a WebGL-compatible interactive graph system in PixiJS.
- We must unify the underlying data format (JSON) so that the C++ editor and the Web editor output identical schema configurations.
