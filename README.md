# Project 1 — RPG Character Creator (COMP 163)

## Game Concept
A simple text-based RPG character creator that allows players to create one of four classes (Warrior, Mage, Rogue, Cleric), save to a file, load from a file, view stats, and level up. Stats scale by level using deterministic formulas.

## How to run
1. (Optional) Activate virtual environment:
   - Windows (PowerShell): `.\venv\Scripts\Activate`
2. Install test framework (optional for local testing):
   - `python -m pip install pytest`
3. Run interactive program:
   - `python project1_starter.py`
4. Run unit tests:
   - `python -m pytest tests/test_character_creation.py -v`
   - or `python -m pytest -v` to run all tests.

## Design choices & stat formulas
- Stats are computed by `calculate_stats(character_class, level)`.
  - Warrior: `strength = 10 + level*5`, `magic = 2 + level*1`, `health = 100 + level*10`
  - Mage: `strength = 3 + level*2`, `magic = 12 + level*5`, `health = 80 + level*6`
  - Rogue: `strength = 7 + level*3`, `magic = 6 + level*2`, `health = 70 + level*5`
  - Cleric: `strength = 6 + level*3`, `magic = 10 + level*4`, `health = 95 + level*8`
- All characters start at level 1 with 100 gold. Leveling up increases level and recalculates stats; leveling grants +50 gold.

## File format
Saved files use the exact format required by tests:

## Error handling
- `load_character()` handles `FileNotFoundError` and returns `None` on failure.
- `save_character()` handles `PermissionError` and returns `False` upon failure.
- `create_character()` validates class; if invalid, returns `None`.

## AI Usage
I used ChatGPT to help structure file I/O error handling, fix syntax issues, and craft the `README` and comments. I wrote, tested, and understand every line and can explain it in the interview.

## What I would change next (optional)
- Add starting equipment and a backstory generator.
- Add save directory support and simple battles.

