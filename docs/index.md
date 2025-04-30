# PPMenu Documentation

Welcome to the official documentation for **ppmenu** –  
a clean, fast, and powerful pure Python terminal menu system.

## What is `ppmenu`?

`ppmenu` is a lightweight library for creating  
beautiful and responsive terminal menus with:

- Quick-jump keys
- Vim-style navigation
- ALT+key support
- Submenus
- Real-time dynamic displays (like a cart or quiz score)

All this with **zero dependencies**, and designed to be easy to extend.

---

## 📦 Installation

```bash
uv pip install ppmenu
```

Or, without `uv`:

```bash
pip install ppmenu
```

---

## 🚀 Quick Start (Pure Structure)

```python
from ppmenu import PPM

# Define logic

def say_hello() -> None:
    print("Hello!")

def quit_program() -> None:
    exit()

# Map logic to keys via clean dict
COMMANDS = {
    'hello': say_hello,
    'quit': quit_program,
}

# Menu structure
MENU_STRUCTURE = {
    '[h] Hello': COMMANDS['hello'],
    '[q] Quit': COMMANDS['quit'],
}

PPM(menu_structure=MENU_STRUCTURE, title='My First Menu').run()
```

---

## 📚 Contents

- [HOWTO: Step-by-Step Guide](howto.md)
- [Examples Overview](examples.md)
- [Advanced Usage](advanced.md)
- [API Reference](api.md)
- [Contributing](contributing.md)

---

# HOWTO: Step-by-Step Guide

This guide walks you through building interactive terminal menus step by step using `ppmenu` — the clean, dictionary-first way.

---

## 1. Define Logic Separately

```python
def add_item(name: str) -> None:
    print(f"Added {name}")

def exit_app() -> None:
    exit()
```

---

## 2. Declare Data Using Pure Dictionaries

```python
PRODUCTS = {
    'Fruits': {
        'a': 'Apple',
        'b': 'Banana',
        None: 'Grapes',
    },
    'Vegetables': {
        'c': 'Carrot',
        None: 'Broccoli',
        't': 'Tomato',
    },
    'Other': {
        'x': 'Mystery Box',
        None: 'Water',
    },
}
```

---

## 3. Build Menu from Data

```python
MENU = {}

for section, items in PRODUCTS.items():
    submenu = {}
    for key, name in items.items():
        label = f'[{key}] {name}' if key else name
        submenu[label] = lambda n=name: add_item(n)
    MENU[f'[{section[0].lower()}] {section}'] = submenu

MENU['[q] Quit'] = exit_app
```

---

## 4. Create and Run the Menu

```python
from ppmenu import PPM

PPM(menu_structure=MENU, title='Fruit Selector').run()
```

---

## 5. ALT Quick-Jump Support

To use `[h]`, `[j]`, `[k]`, or `[l]` as quick-jump keys without breaking Vim navigation, press `Alt+h`, `Alt+j`, etc.

---

## 6. Dynamic Content Display

Override `_display_cart()` or `_display_title()` in your custom class:

```python
from ppmenu import PPM

class MyMenu(PPM):
    def _display_cart(self):
        print("🧾 Current Selection:")
        print(" - Apple\n - Carrot")
```

---

## 7. Customize Colors

If you want to override default settings.

```python
from ppmenu import ColorScheme

colors = ColorScheme(
    title='\033[1;35m',
    selected='\033[1;32m',
    submenu='\033[1;36m',
    quick_letter='\033[1;33m',
)
```

Pass it to your menu:

```python
MyMenu(menu_structure=MENU, title='Styled Demo', colors=colors).run()
```

---

## 8. Run Full Examples

```bash
python examples/demo.py
python examples/coffee_shop.py
python examples/english_quiz.py
```

Each one uses clean, separated data + logic + structure.

---

Made with ❤️ by Sergey Samoylov  
Licensed under GPLv3

