player_class = ["Warrior", "Knight", "Wizard", "Mage", "Archer", "Rogue"]

player_class = "Warrior"

match player_class:
    case "Warrior":
        health = 150
        damage = 20
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case "Knight":
        health = 175
        damage = 25
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case "Wizard":
        health = 50
        damage = 50
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case "Mage":
        health = 80
        damage = 35
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case "Archer":
        health = 100
        damage = 25
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case "Rogue":
        health = 90
        damage = 30
        print(f"Deze class heeft {health} health en doet {damage} damage.")
    case _:
        health = 0
        damage = 0
        print(f"Onbekende class.")