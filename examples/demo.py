#!/usr/bin/env python3

import sys

from ppmenu import PPM, ColorScheme

# Simulated cart
cart: list[str] = []

def add_to_cart(name: str) -> None:
    cart.append(name)

def quit_demo() -> None:
    print("\nThanks for trying out PPMenu!")
    sys.exit(0)

# Item database
ITEMS = {
    'Fruits': {
        'a': 'Apple',
        'b': 'Banana',
        None: 'Grapes',  # No quick jump
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

# Build menu dynamically
menu_structure = {}

for category, items in ITEMS.items():
    submenu = {}
    for key, name in items.items():
        display = f'[{key}] {name}' if key else name
        submenu[display] = lambda n=name: add_to_cart(n)
    menu_structure[f'[{category[0].lower()}] {category}'] = submenu

menu_structure['About'] = lambda: print("\nppMenu is a pure Python menu system.")
menu_structure['[q] Quit'] = quit_demo

class DemoMenu(PPM):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "✨ Welcome to ppMenu Demo ✨"

    def _display_cart(self) -> None:
        print(f"{self.colors.submenu}Selected Items:{self.colors.reset}")
        if cart:
            for item in cart:
                print(f" - {item}")
        else:
            print(" (none)")
        print()

if __name__ == "__main__":
    colors = ColorScheme(
        title='\033[1;33m',
        selected='\033[1;32m',
        submenu='\033[1;36m',
        quick_letter='\033[1;35m',
    )
    DemoMenu(
        menu_structure=menu_structure,
        colors=colors,
        show_nav_help=True,
    ).run()

