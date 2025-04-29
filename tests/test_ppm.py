import pytest

from ppmenu import PPM, PPMError


# --- Fixtures ---

@pytest.fixture
def sample_menu():
    return {
        '[f] File': {
            '[n] New': lambda: None,
            '[o] Open': lambda: None,
        },
        '[e] Edit': {
            '[u] Undo': lambda: None,
            '[r] Redo': lambda: None,
        }
    }

@pytest.fixture
def ppm_instance(sample_menu):
    return PPM(menu_structure=sample_menu, title='Test Menu')


# --- Tests ---

def test_process_menu_structure_basic(ppm_instance):
    assert '[f] File' not in ppm_instance.menu
    assert 'File' in ppm_instance.menu
    assert ppm_instance.menu['File'].quick_nav == 'f'
    assert ppm_instance.menu['Edit'].quick_nav == 'e'

def test_duplicate_quick_nav_key_raises():
    menu = {
        '[h] Help': lambda: None,
        '[h] Home': lambda: None,
    }
    with pytest.raises(PPMError) as excinfo:
        PPM(menu_structure=menu)
    assert 'Duplicate quick jump letter' in str(excinfo.value)

def test_empty_menu_raises():
    with pytest.raises(PPMError) as excinfo:
        PPM(menu_structure={})
    assert 'Empty menu structure' in str(excinfo.value)

def test_quick_jump_normal_letter(ppm_instance, monkeypatch):
    # Simulate user pressing 'f' to jump to [f] File
    monkeypatch.setattr(ppm_instance, '_getch', lambda: 'f')
    new_level = ppm_instance._handle_navigation(ppm_instance.menu)
    assert new_level is not None
    assert isinstance(new_level, dict)

def test_alt_quick_jump_hjkl(ppm_instance, monkeypatch):
    # Simulate user pressing ALT+h (to quick-jump to an item with [h])
    # First, add a submenu with [h] key
    ppm_instance.menu['Help'] = ppm_instance.menu['File']
    ppm_instance.menu['Help'].quick_nav = 'h'
    ppm_instance.menu['Help'].original_key = '[h] Help'
    ppm_instance.menu['Help'].quick_nav_map['h'] = 0

    monkeypatch.setattr(ppm_instance, '_getch', lambda: 'ALT+h')
    new_level = ppm_instance._handle_navigation(ppm_instance.menu)
    assert new_level is not None

def test_navigation_movement(ppm_instance, monkeypatch):
    # Simulate pressing 'j' (move down)
    monkeypatch.setattr(ppm_instance, '_getch', lambda: 'j')
    ppm_instance.current_pos = 0
    new_level = ppm_instance._handle_navigation(ppm_instance.menu)
    assert ppm_instance.current_pos == 1

    # Simulate pressing 'k' (move up)
    monkeypatch.setattr(ppm_instance, '_getch', lambda: 'k')
    new_level = ppm_instance._handle_navigation(ppm_instance.menu)
    assert ppm_instance.current_pos == 0

def test_submenu_navigation(ppm_instance, monkeypatch):
    # Simulate pressing 'f' to enter File submenu
    monkeypatch.setattr(ppm_instance, '_getch', lambda: 'f')
    new_level = ppm_instance._handle_navigation(ppm_instance.menu)
    assert isinstance(new_level, dict)
    assert '[n] New' in new_level or 'New' in new_level

