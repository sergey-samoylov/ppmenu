# API Reference

This is the complete API reference for `ppmenu`.

---

## `class PPM`

Main class for creating and displaying terminal menus.

### `__init__(...)`

```python
def __init__(
    self,
    menu_structure: dict[str, Any],
    title: Optional[str] = None,
    colors: ColorScheme = DEFAULT_COLORS,
    show_nav_help: bool = True,
)
```

**Arguments:**

- `menu_structure`: Dictionary-based menu definition.
- `title`: Optional string title shown at the top of the menu.
- `colors`: A `ColorScheme` object to define menu coloring.
- `show_nav_help`: Show navigation help at the bottom of the screen.

---

### `run() -> None`

Starts the menu loop.  
Clears the screen and enters interactive mode.

```python
menu = PPM(menu_structure=..., title="My Menu")
menu.run()
```

---

### `menu_structure`

`dict[str, Any]`  
Structure of the menu. Can contain submenus and callable actions.

---

### `title: Optional[str]`

Title text shown at the top of the menu (unless overridden by `_display_title()`).

---

## `class ColorScheme`

Defines ANSI color styles for various parts of the menu.

### Fields:

- `title: str`
- `selected: str`
- `submenu: str`
- `quick_letter: str`
- `brackets: str`
- `dim: str`
- `reset: str`

### Example:

```python
colors = ColorScheme(
    title='\033[1;35m',
    selected='\033[1;32m',
    submenu='\033[1;36m',
    quick_letter='\033[1;33m',
)
```

---

## 🧩 Overridable Methods

These methods can be redefined in a subclass to customize behavior.

### `_display_title() -> None`

Prints the title above the menu.  
Override to print a dynamic or custom title.

```python
def _display_title(self):
    print("🌟 My Custom Title")
```

---

### `_display_cart() -> None`

Called below the title, before the menu.  
Override this to display user selection state, score, cart, etc.

```python
def _display_cart(self):
    for item in self.cart:
        print(f"🛒 {item}")
```

---

### `_display_footer() -> None`

Shows navigation help.  
Override to hide or customize footer info.

---

## `class PPMError(Exception)`

Custom exception raised when the menu is invalid (e.g. empty menu, duplicate keys).

---

## ALT + Quick-Jump Handling

Reserved keys `[h]`, `[j]`, `[k]`, `[l]` can only be triggered with `Alt+key`.

- `h` = move left
- `Alt+h` = jump to `[h]` item
- Same for `j`, `k`, `l`

This avoids conflicts with Vim-style movement.

---

## Utilities (from `constants.py`)

### `Keys`

Predefined key codes for navigation:

- `ARROW_UP`, `ARROW_DOWN`, `ARROW_LEFT`, `ARROW_RIGHT`
- `ENTER`, `NEWLINE`, `ESCAPE`
- Vim keys: `H`, `J`, `K`, `L`

### `ANSI`

Terminal sequences:

- `CLEAR_SCREEN`
- `CLEAR_LINE`
- `CURSOR_HOME`

You usually won’t need to access these directly.

---

## Summary

- Use `PPM` to build and run menus
- Subclass it to customize layout
- Use `ColorScheme` for styling
- Avoid lambdas in structures — keep logic and data separate
- Use `Alt+key` for `[h]`, `[j]`, `[k]`, `[l]`

---

Made with ❤️ by Sergey Samoylov  
Licensed under GPLv3
