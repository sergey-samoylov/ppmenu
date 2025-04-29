#!/usr/bin/env python3
"""A simple, functional terminal menu system with quick-jump and navigation."""

# created by Sergey Samoylov https://github.com/sergey-samoylov/ppmenu

import re
import sys
import termios
import tty

from dataclasses import dataclass
from typing import Any, Callable, Optional

from .constants import ANSI, ColorScheme, DEFAULT_COLORS, Keys, NAVIGATION_HELP


class PPMError(Exception):
    """Custom exception for Pure Python Menu errors."""
    pass


@dataclass
class MenuItem:
    value: Any
    quick_nav: Optional[str]
    original_key: str
    quick_nav_map: dict[str, int]


class PPM:
    """Pure Python Menu system with perfect quick-jump navigation."""

    def __init__(
        self,
        menu_structure: dict[str, Any],
        title: Optional[str] = None,
        colors: ColorScheme = DEFAULT_COLORS,
        show_nav_help: bool = True,
    ):
        """
        Initialize the menu system.

        Args:
            menu_structure: Dictionary structure of the menu.
            title: Optional title displayed above the menu.
            colors: Color scheme instance.
            show_nav_help: Whether to display navigation help.
        """
        if not menu_structure:
            raise PPMError('Empty menu structure provided.')

        self.original_menu = menu_structure
        self.menu = self._process_menu_structure(menu_structure.copy())
        self.title = title
        self.colors = colors
        self.show_nav_help = show_nav_help

        self.current_pos: int = 0
        self.path: list[tuple[dict[str, MenuItem], int]] = []
        self.running: bool = True
        self.arrow_buffer: str = ''

    # --- Menu Processing ---

    def _process_menu_structure(
        self,
        menu: dict[str, Any]
    ) -> dict[str, MenuItem]:
        """
        Process raw menu into structured MenuItem instances.

        Args:
            menu: Raw menu dictionary.

        Returns:
            Processed menu dictionary.
        """
        processed: dict[str, MenuItem] = {}
        quick_nav_map: dict[str, int] = {}

        for idx, (key, value) in enumerate(menu.items()):
            match = re.match(r'^\[([a-z])\]\s+(.*)', key, re.IGNORECASE)
            if match:
                quick_nav = match.group(1).lower()
                new_key = match.group(2).strip()
                if quick_nav in quick_nav_map:
                    raise PPMError(f'Duplicate quick jump letter: [{quick_nav}] detected.')
                processed[new_key] = MenuItem(
                    value=value,
                    quick_nav=quick_nav,
                    original_key=key,
                    quick_nav_map=quick_nav_map,
                )
                quick_nav_map[quick_nav] = idx
            else:
                processed[key] = MenuItem(
                    value=value,
                    quick_nav=None,
                    original_key=key,
                    quick_nav_map=quick_nav_map,
                )

        return processed

    def _get_quick_nav_map(
        self,
        current_level: dict[str, MenuItem]
    ) -> dict[str, int]:
        """Return quick navigation map for the current level."""
        if not current_level:
            return {}
        first_item = next(iter(current_level.values()))
        return first_item.quick_nav_map

    # --- Terminal Input ---

    def _getch(self) -> str:
        """Capture a single character from stdin, handling arrows and Alt."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)

            if ch == Keys.ESCAPE:
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    return Keys.ESCAPE + '[' + ch3  # Arrow keys
                return f'ALT+{ch2.lower()}'  # Alt+key

            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # --- Display Methods ---

    def _clear_screen(self) -> None:
        """Clear the terminal screen."""
        print(ANSI.CLEAR_SCREEN, end='')

    def _display_menu(self, current_level: dict[str, MenuItem]) -> None:
        """Master function to display the menu."""
        self._clear_screen()
        self._display_title()
        self._display_cart()
        self._display_menu_items(current_level)
        self._display_footer()

    def _display_title(self) -> None:
        """Display the menu title."""
        if self.title:
            print(f'{self.colors.title}{self.title}{self.colors.reset}\n')

    def _display_cart(self) -> None:
        """Optional cart/status display. Empty by default."""
        pass

    def _display_menu_items(self, current_level: dict[str, MenuItem]) -> None:
        """Display all menu items."""
        items = list(current_level.items())
        for i, (key, item) in enumerate(items):
            prefix = (
                f'{self.colors.selected}-> {self.colors.reset}'
                if i == self.current_pos else '   '
            )
            quick_nav = item.quick_nav
            value = item.value
            original_key = item.original_key

            if i == self.current_pos:
                display_text = self._format_selected_item(quick_nav, original_key)
            else:
                display_text = self._format_unselected_item(quick_nav, original_key, value)

            print(f'{prefix}{display_text}')

    def _format_selected_item(self, quick_nav: Optional[str], text: str) -> str:
        """Format selected item line."""
        if quick_nav:
            return (
                f'{self.colors.brackets}[{self.colors.reset}'
                f'{self.colors.selected}{quick_nav}{self.colors.reset}'
                f'{self.colors.brackets}]{self.colors.reset}'
                f'{self.colors.selected}{text[3:]}{self.colors.reset}'
            )
        return f'{self.colors.selected}{text}{self.colors.reset}'

    def _format_unselected_item(
        self,
        quick_nav: Optional[str],
        text: str,
        value: Any
    ) -> str:
        """Format unselected item line."""
        color = (
            self.colors.submenu if isinstance(value, dict)
            else self.colors.dim
        )
        if quick_nav:
            return (
                f'{self.colors.brackets}[{self.colors.reset}'
                f'{self.colors.quick_letter}{quick_nav}{self.colors.reset}'
                f'{self.colors.brackets}]{self.colors.reset}'
                f'{color}{text[3:]}{self.colors.reset}'
            )
        return f'{color}{text}{self.colors.reset}'

    def _display_footer(self) -> None:
        """Display navigation help."""
        if self.show_nav_help:
            print(NAVIGATION_HELP)

    # --- Navigation Handling ---

    def _handle_navigation(
        self,
        current_level: dict[str, MenuItem]
    ) -> Optional[dict[str, MenuItem]]:
        """Handle user input for navigation and selection."""
        char = self._getch()
        quick_nav_map = self._get_quick_nav_map(current_level)

        # ALT+Quick Jump
        if char.startswith('ALT+'):
            alt_key = char[4:]
            if alt_key in quick_nav_map:
                self.current_pos = quick_nav_map[alt_key]
                return self._activate_item(current_level, self.current_pos)
            return current_level

        # Normal Quick Jump (except h/j/k/l)
        if (
            len(char) == 1
            and char.lower() in quick_nav_map
            and char.lower() not in {'h', 'j', 'k', 'l'}
        ):
            self.current_pos = quick_nav_map[char.lower()]
            return self._activate_item(current_level, self.current_pos)

        # Vim-style navigation
        if char in (Keys.ARROW_UP, Keys.K):
            self.current_pos = max(self.current_pos - 1, 0)
            return current_level
        if char in (Keys.ARROW_DOWN, Keys.J):
            self.current_pos = min(self.current_pos + 1, len(current_level) - 1)
            return current_level
        if char in (Keys.ARROW_LEFT, Keys.H):
            if self.path:
                prev_level, prev_pos = self.path.pop()
                self.current_pos = prev_pos
                return prev_level
            return current_level
        if char in (Keys.ARROW_RIGHT, Keys.L, Keys.ENTER, Keys.NEWLINE):
            return self._activate_item(current_level, self.current_pos)
        if char == Keys.Q:
            self.running = False
            return None

        return current_level

    def _activate_item(
        self,
        current_level: dict[str, MenuItem],
        pos: int
    ) -> Optional[dict[str, MenuItem]]:
        """Activate the menu item at the given position."""
        if not current_level or pos >= len(current_level):
            return current_level

        key = list(current_level.keys())[pos]
        item = current_level[key]
        value = item.value

        if callable(value):
            self._clear_screen()
            value()
            return current_level
        if isinstance(value, dict) and value:
            self.path.append((current_level, self.current_pos))
            self.current_pos = 0
            return self._process_menu_structure(value)

        print(f'\nSelected: {key} -> {value}')
        return current_level

    # --- Main Loop ---

    def run(self) -> None:
        """Run the menu system."""
        current_level = self.menu
        while self.running:
            self._display_menu(current_level)
            new_level = self._handle_navigation(current_level)
            if new_level is not current_level:
                current_level = new_level or self.menu

