import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    weaponRoll = random.randint(1, 6)
    print(f"Weapon Roll: {weaponRoll}")

    heroCombatStrength = 200
    heroCombatStrength += weaponRoll

    heroWeapon = weapons[weaponRoll - 1]
    print(f"Hero's Weapon: {heroWeapon}")

    if weaponRoll <= 2:
        print("You rolled a weak weapon")
    elif weaponRoll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon friend")
    if heroWeapon != weapons[0]:
        print("Thank goodness you didn't roll the Fist...")

except Exception as e:
    print(f"An error occurred: {e}")
