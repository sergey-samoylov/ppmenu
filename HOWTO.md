# 📚 HOWTO: Build Menus with `ppmenu`

Welcome! This guide walks you through building interactive terminal menus step
by step using `ppmenu`.

---

## 1. Install `ppmenu`

```bash
uv pip install ppmenu
```

Or if not using `uv`:

```bash
pip install ppmenu
```

---

## 2. Minimal Example

Here's the smallest working menu:

```python
from ppmenu import PPM

menu = {
    '[h] Hello': lambda: print('Hello!'),
    '[q] Quit': lambda: exit(0),
}

PPM(menu_structure=menu, title='My First Menu').run()
```

✅ For navigation use arrow keys or Vim keys (`h/j/k/l`)

---

## 3. Adding Submenus

```python
menu = {
    '[f] File': {
        '[n] New': lambda: print('New file'),
        '[s] Save': lambda: print('Saved!'),
    },
    '[q] Quit': lambda: exit(0),
}
```

---

## 4. Displaying Dynamic Content (e.g., a Cart)

Subclass `PPM` to override `_display_cart()`:

```python
from ppmenu import PPM

class MyMenu(PPM):
    def _display_cart(self):
        print('🛒 Your cart: ...')

MyMenu(menu_structure=..., title='With Cart').run()
```

---

## 5. ALT + Quick-Jump Support

To jump to `[h]`, `[j]`, `[k]`, or `[l]`, use `Alt+h`, `Alt+j`, etc.  
✅ This avoids conflict with Vim navigation keys.

---

## 6. Example: English Quiz

```python
QUESTIONS = {
    'go': ('went', ['goed', 'went', 'go']),
    ...
}
```

Dynamically build the menu using clean Python logic.

Check `examples/english_quiz.py` for full source.

---

## 7. Tips

- Use `[x] Label` format for quick jumps
- Use `None` keys for items without quick jumps
- Group logic in a clean structure — no manual repetition!
- Use `ColorScheme` to customize how your menu looks

---

## 8. Full Demo

```bash
python examples/demo.py
```

---

## 9. Learn More

- [README.md](./README.md)
- [examples/](./examples/)
- [tests/](./tests/)

---

Made with ❤️ by Sergey Samoylov  
License: [GNU GPLv3](LICENSE)

