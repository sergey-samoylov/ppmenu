# Advanced Usage

This guide explores advanced capabilities of `ppmenu`,  
such as customization, dynamic behavior, and ways to extend or adapt  
the system to your needs.

---

## 🎨 Subclassing `PPM`

You can customize any aspect of the menu by subclassing `PPM`.

### Example: Custom Title and Cart Display

```python
from ppmenu import PPM

class MyMenu(PPM):
    def _display_title(self):
        print("📦 Welcome to My Custom Menu\n")  # Custom title

    def _display_cart(self):
        print("🧾 You selected:")
        for item in self.cart:
            print(f" - {item}")

# Run it
MyMenu(menu_structure=..., title=None).run()
```

---

## 🌀 Dynamic Menu Generation

You can build menus based on user data, file input, or runtime state.

### Example: Build Menu from a JSON File

```python
import json

with open('items.json') as f:
    data = json.load(f)

MENU = {
    f'[{i[0].lower()}] {i}': lambda n=i: print(f"Selected {n}")
    for i in data['options']
}
```

---

## ⌨️ ALT + Quick-Jump Logic

To avoid conflicts with Vim-style keys (`h`, `j`, `k`, `l`), `ppmenu` supports:

- Normal quick-jumps: `[a]`, `[f]`, `[m]`, etc. via single key
- Reserved keys: `[h]`, `[j]`, `[k]`, `[l]` require **Alt+key** (e.g., Alt+j)

Under the hood, your terminal sends:  
`ESC + key` → interpreted as `ALT+<key>`

---

## 🖌️ Themes with `ColorScheme`

Create consistent menu themes by customizing the `ColorScheme` class.

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
MyMenu(menu_structure=MENU, colors=colors).run()
```

---

## 🧱 Clean Architecture Tips

- ✅ **Data-first**: Use pure dicts (`PRODUCTS`, `QUESTIONS`)
- ✅ **Logic separate from structure**
- ✅ **Menu built dynamically** from clean mappings
- ❌ Avoid inline lambdas in menu structures

---

## 🔌 Future Extensions (Ideas)

You can extend `ppmenu` by:

- Adding **plugin hooks** (e.g. `on_enter`, `on_quit`)
- Supporting **asynchronous calls** (for networked menus)
- Building a **menu stack system** (stack of PPM instances)
- Adding simple **animations or transitions** (spinner, blink, typewriter effect)
- Creating **layout presets** (vertical, horizontal, grid menus)

Want to contribute any of these? See [CONTRIBUTING.md](contributing.md)

---

## 📎 Summary

With subclassing and clean architecture, `ppmenu` can support everything from:

- Quizzes
- Inventory tools
- RPG selection screens
- Dev dashboards
- System CLI tools
- Multi-language teaching apps

Built clean. Run fast. Stay Pythonic.

---

Made with ❤️ by Sergey Samoylov  
Licensed under GPLv3
