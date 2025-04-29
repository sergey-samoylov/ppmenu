# PPMENU Code Style Guide

## 📐 `CODE_STYLE.md`

This guide defines the coding conventions used in the `ppmenu` project.

All contributions and internal code must follow this guide to ensure consistency,  
readability, and long-term maintainability.

---

## ✅ General Philosophy

- **Readability first.**
- Follow the **DRY** (Don't Repeat Yourself) principle.
- Prefer **explicit** and **descriptive** code over clever tricks.
- Write code that is easy to modify and extend.

---

## 🧱 Project Structure

```
ppmenu/
    __init__.py
    constants.py
examples/
    demo.py
    CozyCoffeeShop/
        coffee_quotes.py
        coffee_shop.py
    EnglishQuiz/
        english_quiz.py
tests/
    test_ppm.py
```

- `ppmenu/`: Core library
- `examples/`: All demo apps showing usage
- `tests/`: Pytest-based test suite

---

## 🐍 Python Style (PEP8 + enhancements)

### ✅ Required:
- Max line length: **79 characters**
- Use **4 spaces** for indentation
- All functions and classes must have **docstrings**
- Use **single quotes `'`** for strings, unless double quotes help avoid escapes

---

## 🧠 Type Hints

- All functions **must** include full type hints
- Example:

```python
def add_to_cart(name: str) -> None:
    ...
```

---

## 📖 Docstrings

- Use short one-liners or full multiline format
- Required for **all public functions, classes, and methods**
- Follow this format:

```python
def run(self) -> None:
    """Starts the interactive menu loop."""
```

---

## 🎨 Naming Conventions

| Item | Convention | Example |
|:---|:---|:---|
| Classes | `CamelCase` | `PPM`, `CoffeeShopMenu` |
| Functions | `snake_case` | `add_to_cart`, `finish_quiz` |
| Variables | `snake_case` | `menu_structure`, `quiz_answers` |
| Constants | `ALL_CAPS` | `DEFAULT_COLORS`, `NAVIGATION_HELP` |

---

## 📚 Imports

- Standard library imports go first
- Then third-party (if any)
- Then local `ppmenu` imports
- Group with one empty line between blocks

✅ Example:

```python
import sys

from typing import Optional

from ppmenu import PPM, ColorScheme
```

---

## 🧼 DRY Code Guidelines

- Always build menu structures **dynamically** from clean dicts
- Never hardcode duplicate labels or handlers
- Prefer:

```python
for key, name in PRODUCTS.items():
    ...
```

over:

```python
'[a] Apple': lambda: ...
'[b] Banana': lambda: ...
```

---

## 📋 Menu Keys

- Use `[x] Label` format for quick-jump items
- Use `None: 'Item'` for items without quick-jump
- Keys must be lowercase, single characters (enforced by parser)

✅ Valid:

```python
'[a] Apple'
'[q] Quit'
```

---

## 🧪 Testing Style

- Use **pytest**
- All test files live in `tests/`
- Use `monkeypatch` for input mocking
- Test cases must:
  - Cover functionality
  - Handle edge cases
  - Validate clean exits

---

## 📝 Examples and Demos

- All demos must live in `examples/`
- Each must show real use of `ppmenu`
- Should subclass `PPM` and override at least one method (`_display_cart()` or `_display_title()`)

---

## 📜 License Compliance

- This project uses **GNU GPLv3**
- All files must retain the license (add header if needed for scripts)

---

## 📦 PyPI Readiness

- All code must work standalone after install via `pip install ppmenu`
- No dependencies
- Public interface is `from ppmenu import PPM, ColorScheme`

---

## 💡 Tip: Use EditorConfig or Black?

This project prefers **manual formatting** over auto-formatters.

> Black is not enforced to allow for better visual control at 79 chars.

---

## ✅ Summary

Follow this guide and your contributions will:

- Match the rest of the project
- Be easy to maintain and extend
- Help keep `ppmenu` clean, useful, and professional

Happy coding! 🎉

---

## Contributing

📢Please follow the [Code Style Guide](CODE_STYLE.md) before submitting pull requests.

