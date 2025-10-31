"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Matthew Solomon
Date: 10/28/2025

AI Usage: ChatGPT assisted with structuring the file I/O error handling,
stat-balancing formulas, and formatting to match COMP 163 test requirements.
I reviewed, tested, and can explain every line.
"""

# ==============================
#  CHARACTER CREATION FUNCTIONS
# ==============================

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns a tuple (strength, magic, health).
    """
    if character_class == "Warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 100 + (level * 10)
    elif character_class == "Mage":
        strength = 3 + (level * 2)
        magic = 12 + (level * 5)
        health = 80 + (level * 6)
    elif character_class == "Rogue":
        strength = 7 + (level * 3)
        magic = 6 + (level * 2)
        health = 70 + (level * 5)
    elif character_class == "Cleric":
        strength = 6 + (level * 3)
        magic = 10 + (level * 4)
        health = 95 + (level * 8)
    else:
        # Fallback neutral stats if invalid class
        strength, magic, health = 5, 5, 50

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns a dictionary containing all attributes.
    """
    # Validate class
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Error: Invalid class name.")
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


def save_character(character, filename):
    """
    Saves a character to a text file in the required format.
    Returns True if successful, False if an error occurs.
    """
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except PermissionError:
        print("Error: Permission denied while saving file.")
        return False
    except Exception as e:
        print("Error while saving:", e)
        return False


def load_character(filename):
    """
    Loads character data from file and returns a dictionary.
    Returns None if file not found or invalid.
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return None

    data = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip()

    try:
        character = {
            "name": data.get("Character Name", ""),
            "class": data.get("Class", ""),
            "level": int(data.get("Level", 1)),
            "strength": int(data.get("Strength", 0)),
            "magic": int(data.get("Magic", 0)),
            "health": int(data.get("Health", 0)),
            "gold": int(data.get("Gold", 0))
        }
        return character
    except Exception as e:
        print("Error loading character:", e)
        return None


def level_up(character):
    """
    Increases the character's level by one and recalculates stats.
    Returns the updated character dictionary.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50  # bonus gold per level-up
    return character


def display_character(character):
    """
    Displays character information in readable format.
    """
    print(f"Character Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# ==============================
#  DEMO TESTING SECTION
# ==============================
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    if hero:
        print("Character created successfully!")
        display_character(hero)

        if save_character(hero, "aria.txt"):
            print("\nCharacter saved successfully.")

        loaded = load_character("aria.txt")
        if loaded:
            print("\nLoaded character:")
            display_character(loaded)

        print("\nLeveling up character...")
        leveled = level_up(hero)
        display_character(leveled)
