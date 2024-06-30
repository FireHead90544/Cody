import time
import sys

# Define colors
COLORS = {
    'intro': '\033[92m',  # Green
    'house': '\033[93m',  # Yellow
    'fight': '\033[91m',  # Red
    'cave': '\033[94m',   # Blue
    'end': '\033[0m'      # End color
}

# Function to display text character by character
def print_quest(string, speed=0.1):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Function to display the introduction of the game
def display_intro():
    intro_statements = [
        ("Welcome to the Adventure Game!", 0.1, 'intro'),
        ("You find yourself standing in an open field, filled with grass and yellow wildflowers.", 0.05, 'intro'),
        ("Rumor has it that a great treasure is hidden somewhere in this field.", 0.05, 'intro'),
        ("In front of you is a house.", 0.05, 'intro'),
        ("To your right is a dark cave.", 0.05, 'intro'),
        ("In your hand you hold your trusty (but not very effective) dagger.", 0.05, 'intro')
    ]
    for statement, speed, color in intro_statements:
        print_quest(COLORS[color] + statement + COLORS['end'], speed)
        time.sleep(2)

# Function to handle the house scenario
def house():
    house_statements = [
        ("\nYou approach the door of the house.", 0.05, 'house'),
        ("You are about to knock when the door opens and out steps a goblin.", 0.05, 'house'),
        ("Eep! This is the goblin's house!", 0.05, 'house'),
        ("The goblin attacks you!", 0.05, 'house')
    ]
    for statement, speed, color in house_statements:
        print_quest(COLORS[color] + statement + COLORS['end'], speed)
        time.sleep(2)

    action = input("Do you (1) fight or (2) run away? ")
    
    if action == "1":
        fight_statements = [
            ("You feel a bit under-prepared for this, what with only having a tiny dagger.", 0.05, 'fight'),
            ("You do your best...", 0.05, 'fight'),
            ("but your dagger is no match for the goblin.", 0.05, 'fight'),
            ("You have been defeated!", 0.05, 'fight')
        ]
        for statement, speed, color in fight_statements:
            print_quest(COLORS[color] + statement + COLORS['end'], speed)
            time.sleep(2)
    elif action == "2":
        print_quest(COLORS['house'] + "You run back into the field. Luckily, you don't seem to have been followed." + COLORS['end'], 0.05)

# Function to handle the cave scenario
def cave():
    cave_statements = [
        ("\nYou peer cautiously into the cave.", 0.05, 'cave'),
        ("It turns out to be only a very small cave.", 0.05, 'cave'),
        ("Your eye catches a glint of metal behind a rock.", 0.05, 'cave'),
        ("You have found the magical sword of Ogoroth!", 0.05, 'cave'),
        ("You discard your silly old dagger and take the sword with you.", 0.05, 'cave'),
        ("You walk back out to the field.", 0.05, 'cave')
    ]
    for statement, speed, color in cave_statements:
        print_quest(COLORS[color] + statement + COLORS['end'], speed)
        time.sleep(2)

# Main game loop
def main():
    display_intro()
    
    while True:
        print_quest("\nEnter 1 to knock on the door of the house.", 0.1)
        print_quest("Enter 2 to peer into the cave.", 0.1)
        print_quest("What would you like to do?", 0.1)
        action = input("(Please enter 1 or 2.) ")

        if action == "1":
            house()
        elif action == "2":
            cave()
        else:
            print_quest("Invalid input. Please enter 1 or 2.", 0.1)

        print_quest("\nDo you want to play again? (yes or no)", 0.1)
        play_again = input().lower()

        if play_again != "yes":
            break

if __name__ == "__main__":
    main()

