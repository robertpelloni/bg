# bob's game / OKGame Lua API Reference

This document outlines the available Lua bindings for modding the **okgame** (C++) client.

## 1. Core Functions

### `log(message)`
Logs a message to the engine's info log. Prefix: `[Lua]`.
- `message`: (string) The text to log.

### `logError(message)`
Logs an error message to the engine's error log.
- `message`: (string) The text to log.

## 2. Game State

### `getScore()`
Returns the current player's score.
- Returns: (number) Current score.

### `getLevel()`
Returns the current player's level.
- Returns: (number) Current level.

## 3. Grid & Tile Manipulation

### `getGridWidth()`
Returns the width of the puzzle grid in tiles.
- Returns: (number) Grid width.

### `getGridHeight()`
Returns the height of the puzzle grid in tiles.
- Returns: (number) Grid height.

### `getTile(x, y)`
Returns the name of the block type at the specified grid coordinates.
- `x`, `y`: (number) Grid coordinates.
- Returns: (string|nil) Block type name, or `nil` if empty.

### `setTile(x, y, typeName)`
Sets a specific block type at the grid coordinates.
- `x`, `y`: (number) Grid coordinates.
- `typeName`: (string) Name of the block type (e.g., "Normal", "Garbage").

## 4. Piece Information

### `getPieceInfo()`
Returns a table containing information about the currently active piece.
- Returns: (table|nil) A table with the following keys:
    - `x`: (number) X grid position.
    - `y`: (number) Y grid position.
    - `rotation`: (number) Current rotation index.
    - `type`: (string) Name of the piece type.

## 5. Screen & Visual Effects

### `shakeScreen()`
Triggers a small screen shake effect.

### `wiggleScreen()`
Triggers a "wiggle" effect on the playing field.

## 6. Networking & Garbage

### `sendGarbage(amount)`
Queues a specific amount of VS garbage to be sent to opponents.
- `amount`: (number) Number of garbage blocks.

### `receiveGarbage(amount)`
Triggers the immediate reception of a specific amount of garbage.
- `amount`: (number) Number of garbage blocks.

---
*Documentation for version 2.0.0 (Lua 5.1 Integration).*
