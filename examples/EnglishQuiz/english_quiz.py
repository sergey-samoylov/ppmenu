#!/usr/bin/env python3

import sys
from ppmenu import PPM, ColorScheme

# Track answers
answers: list[tuple[str, str, bool]] = []
score = 0

# Quiz data
QUESTIONS = {
    'go': ('went', ['goed', 'went', 'go']),
    'eat': ('ate', ['eated', 'ate', 'eaten']),
    'take': ('took', ['taken', 'took', 'taked']),
    'have': ('had', ['has', 'had', 'haved']),
    'run': ('ran', ['run', 'ranned', 'ran']),
}

def correct(base: str, choice: str) -> None:
    global score
    answers.append((base, choice, True))
    score += 1

def wrong(base: str, choice: str) -> None:
    answers.append((base, choice, False))

def finish_quiz() -> None:
    print(f"\n✅ Finished! Your score: {score}/{len(QUESTIONS)}")
    sys.exit(0)

# Build menu dynamically
menu_structure = {}

for idx, (verb, (correct_form, options)) in enumerate(QUESTIONS.items(), start=1):
    submenu = {}
    for i, opt in enumerate(options):
        key = chr(97 + i)  # a, b, c
        label = f'[{key}] {opt}'
        handler = correct if opt == correct_form else wrong
        submenu[label] = lambda v=verb, o=opt, h=handler: h(v, o)
    menu_structure[f'[{idx}] {verb}'] = submenu

menu_structure['[f] Finish Quiz'] = finish_quiz

class EnglishQuiz(PPM):
    def _display_cart(self) -> None:
        print(f"{self.colors.submenu}Your Answers:{self.colors.reset}")
        for verb, answer, is_correct in answers:
            icon = '✅' if is_correct else '❌'
            print(f"{icon} {verb} → {answer}")
        if answers:
            print(f"\nScore: {score}/{len(QUESTIONS)}\n")
        else:
            print(" (no answers yet)\n")

if __name__ == "__main__":
    colors = ColorScheme(
        title='\033[1;34m',
        selected='\033[1;33m',
        submenu='\033[1;36m',
        quick_letter='\033[1;32m',
    )
    EnglishQuiz(
        menu_structure=menu_structure,
        colors=colors,
        show_nav_help=False,
        title="📘 English Past Simple Quiz",
    ).run()

