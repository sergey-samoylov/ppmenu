# Contributing to `ppmenu`

We welcome contributions!  
If you want to improve `ppmenu`, fix bugs, write documentation,  
or add examples — this guide is for you.

---

## 🛠️ Dev Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourname/ppmenu.git
cd ppmenu
```

### 2. Install dependencies

```bash
uv pip install -e .[dev]
```

Or, if not using `uv`:

```bash
pip install -e .[dev]
```

### 3. Run tests

```bash
pytest
```

Tests are located in the `tests/` directory.

---

## 🧪 Writing Tests

- All tests use **pytest**
- Place them in `tests/`
- Use fixtures and monkeypatching where appropriate
- Mock `_getch()` to simulate keyboard input

Follow examples in `tests/test_ppm.py`.

---

## 💎 Code Style

Please follow our [Code Style Guide](../CODE_STYLE.md):

- PEP8-compliant
- Line length max: 79 characters
- Type hints everywhere
- All functions/classes must have docstrings
- Use pure data dicts (`PRODUCTS`, `QUESTIONS`) — no inline lambdas

---

## 🧩 Adding Examples

Add your demo scripts to the `examples/` folder:

```bash
examples/
├── demo.py
├── english_quiz.py
├── your_demo.py  ← Add here
```

Examples must be:

- Standalone (can be run with `python`)
- DRY (logic, data, structure are separate)
- Use subclassing to customize cart/title when needed

---

## 📄 Documentation

- Edit docs in `docs/` using Markdown (`.md`)
- Update `README.md` and `HOWTO.md` if necessary
- Keep doc examples DRY and idiomatic

---

## 🚀 Submitting Changes

1. Create a feature branch:

```bash
git checkout -b your-feature-name
```

2. Commit your changes with a clear message:

```bash
git commit -m "Add new dynamic menu example"
```

3. Push and open a pull request (PR) on GitHub.

---

## ❤️ Code of Conduct

Be respectful and constructive.
This is a friendly project — beginners welcome!

---

Thank you for helping make `ppmenu` better!  
— Sergey Samoylov  
Licensed under GPLv3
