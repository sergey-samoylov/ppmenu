from dataclasses import dataclass

@dataclass
class Keys:
    ARROW_UP = '\x1b[A'
    ARROW_DOWN = '\x1b[B'
    ARROW_RIGHT = '\x1b[C'
    ARROW_LEFT = '\x1b[D'
    ENTER = '\r'
    NEWLINE = '\n'
    ESCAPE = '\x1b'
    Q = 'q'
    H = 'h'
    J = 'j'
    K = 'k'
    L = 'l'

@dataclass
class ColorScheme:
    title: str = "\033[1;34m"        # Bright blue
    selected: str = "\033[1;36m"     # Bright cyan
    submenu: str = "\033[1;35m"      # Bright magenta
    quick_letter: str = "\033[1;32m" # Bright green
    brackets: str = "\033[1;37m"     # White
    dim: str = "\033[2m"             # Dimmed
    reset: str = "\033[0m"           # Reset

# Default color scheme
DEFAULT_COLORS = ColorScheme()

@dataclass
class ANSI:
    CLEAR_SCREEN = "\033[2J\033[H"
    CLEAR_LINE = "\033[2K"
    CURSOR_HOME = "\033[H"


NAVIGATION_HELP = (
    '\nNavigation:\n'
    ' - j/k or ↓/↑      : Move down/up\n'
    ' - h or ←          : Go back\n'
    ' - l or →/Enter    : Select\n'
    ' - q               : Quit'
)
