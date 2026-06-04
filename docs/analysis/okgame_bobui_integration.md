# `okgame` + `bobui` (Qt6) Integration Guide

## Current State
The `okgame` `CMakeLists.txt` does not currently include the `bobui` submodule. `bobui` is a wrapper around Qt6 designed for building editor interfaces.

## Integration Steps

To enable Qt6 for the `bgeditor` port within the C++ engine:

1. **Modify `okgame/CMakeLists.txt`**:
   Add the `bobui` subdirectory so that CMake configures the Qt6 dependencies.

   ```cmake
   # Enable Qt6 Automoc and Autouic for Qt compilation
   set(CMAKE_AUTOMOC ON)
   set(CMAKE_AUTOUIC ON)
   set(CMAKE_AUTORCC ON)

   # Add bobui library
   add_subdirectory(lib/bobui)

   # Link against bobui in the main executable
   target_link_libraries(${PROJECT_NAME} PRIVATE bobui)
   ```

2. **Refactor `CustomGameEditor.cpp`**:
   The current file relies on raw immediate-mode GUI code wrapped around SDL. We need to bootstrap `bobui`'s `QApplication` instance before the main SDL window spawns (or run them in parallel threads).

   ```cpp
   #include <bobui/MainWindow.h>

   int main(int argc, char* argv[]) {
       // Initialize Qt application for Editor GUI
       QApplication app(argc, argv);
       BobUI::MainWindow editorWindow;
       editorWindow.show();

       // Standard SDL Game Loop ...
   }
   ```
