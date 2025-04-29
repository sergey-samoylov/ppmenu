#!/usr/bin/env python3
"""A Coffee Shop interface done in PPMenu - fast and eyecatching."""

# created by Sergey Samoylov https://github.com/sergey-samoylov/ppmenu

import sys

from ppmenu import PPM, ColorScheme
from coffee_quotes import quotes

# --- Custom Color Scheme ---
custom_colors = ColorScheme(
    title="\033[1;33m",        # Bright yellow
    selected="\033[1;32m",     # Bright green
    submenu="\033[1;36m",      # Bright cyan
    quick_letter="\033[1;35m", # Bright magenta
)

# --- Internal Data ---
cart: list[tuple[str, float]] = []

def add_to_cart(item: str, price: float) -> None:
    """Add an item to the cart."""
    cart.append((item, price))

def view_cart() -> None:
    """Display the cart summary."""
    if not cart:
        print("\nYour cart is empty.")
        return
    print("\nCurrent Cart:")
    total = 0.0
    for name, price in cart:
        print(f"- {name} : ${price:.2f}")
        total += price
    print(f"\nTotal: ${total:.2f}")

def checkout() -> None:
    """Checkout and exit."""
    print(quotes.pop())
    view_cart()
    print("\nThank you for visiting Cozy Coffee Shop!\n")
    sys.exit(0)

def quit_menu() -> None:
    """Exit immediately without checkout."""
    sys.exit(0)

# --- Product Catalog (clean version) ---
PRODUCTS = {
    "Coffee": {
        "e": ("Espresso", 2.50),
        "a": ("Americano", 3.00),
        "l": ("Latte", 4.50),
        "c": ("Cappuccino", 4.00),
        "m": ("Mocha", 4.75),
    },
    "Tea": {
        "g": ("Green Tea", 2.75),
        "b": ("Black Tea", 2.50),
        "h": ("Herbal Tea", 3.00),
        "m": ("Matcha", 4.00),
    },
    "Pastries": {
        "c": ("Croissant", 3.50),
        "m": ("Muffin", 2.75),
        "s": ("Scone", 3.00),
        "d": ("Danish", 3.25),
    },
}

# --- Build menu_structure dynamically ---
menu_structure = {}

for category, items in PRODUCTS.items():
    submenu = {}
    for key, (name, price) in items.items():
        display_name = f"[{key}] {name} - ${price:.2f}"
        submenu[display_name] = lambda n=name, p=price: add_to_cart(n, p)
    menu_structure[f"[{category[0].lower()}] {category}"] = submenu

# Add Order Summary and Quit
menu_structure["[o] Order Summary"] = {
    "[v] View Cart": view_cart,
    "[c] Checkout": checkout,
}
menu_structure["[q] Quit"] = quit_menu

# --- Custom Menu Class ---
class CoffeeShopMenu(PPM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shop_title = "☕ Welcome to Cozy Coffee Shop ☕"

    def _display_title(self) -> None:
        """Display the coffee shop title."""
        print(f"{self.colors.title}{self.shop_title}{self.colors.reset}\n")

    def _display_cart(self) -> None:
        """Display the shopping cart before the menu."""
        print(f"{self.colors.submenu}Current Cart:{self.colors.reset}")
        if cart:
            total = 0.0
            for name, price in cart:
                print(f" - {name} : ${price:.2f}")
                total += price
            print(f"\nTotal: ${total:.2f}\n")
        else:
            quote = next(iter(quotes))
            print(f" {quote}\n")

# --- Run the Coffee Shop Menu ---
def run_coffee_shop() -> None:
    menu = CoffeeShopMenu(
        menu_structure=menu_structure,
        colors=custom_colors,
        show_nav_help=False,
    )
    menu.run()

if __name__ == "__main__":
    run_coffee_shop()

