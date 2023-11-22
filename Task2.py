import time
import random

def introduction():
    print("Welcome to the Mysterious Island Adventure!")
    print("You find yourself on a deserted island. Your goal is to explore and survive.")
    print("Be cautious, as your choices will determine your fate!")

def make_choice(options):
    print("Choose your action:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_island():
    print("\nYou start exploring the island.")

    choices = ["Follow a mysterious path", "Investigate a strange noise", "Build a shelter"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou follow the path and discover a hidden cave.")
        cave()
    elif choice == 2:
        print("\nYou move towards the noise and find a group of friendly animals.")
        animals()
    elif choice == 3:
        print("\nYou decide to build a shelter to protect yourself from the elements.")
        shelter()

def cave():
    print("\nInside the cave, you find a chest.")

    choices = ["Open the chest", "Leave the cave"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou open the chest and find a map to a hidden treasure!")
        treasure_hunt()
    elif choice == 2:
        print("\nYou leave the cave and continue exploring.")
        explore_island()

def animals():
    print("\nThe animals seem to be leading you somewhere.")

    choices = ["Follow the animals", "Stay put"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou follow the animals and discover a magical pond.")
        magical_pond()
    elif choice == 2:
        print("\nYou decide to stay put and observe the animals.")
        print("They leave, and you continue your exploration.")
        explore_island()

def shelter():
    print("\nWith your shelter built, you feel safe.")

    choices = ["Rest in the shelter", "Explore more"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou rest in the shelter and regain your energy.")
        print("Feeling refreshed, you continue your exploration.")
        explore_island()
    elif choice == 2:
        print("\nYou decide to explore more of the island.")
        explore_island()

def magical_pond():
    print("\nThe pond has magical properties.")

    choices = ["Drink from the pond", "Ignore the pond"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou drink from the pond and gain mysterious powers!")
        print("With your new powers, you decide what to do next.")
        ultimate_choice()
    elif choice == 2:
        print("\nYou decide to ignore the pond and continue exploring.")
        explore_island()

def treasure_hunt():
    print("\nThe map leads you to a hidden location.")

    choices = ["Dig for the treasure", "Leave the area"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou dig and find a chest full of treasures!")
        print("Congratulations! You've completed your adventure.")
    elif choice == 2:
        print("\nYou decide to leave the area and explore more of the island.")
        explore_island()

def ultimate_choice():
    print("\nWith your newfound powers, you face a critical decision.")

    choices = ["Use your powers for good", "Use your powers for personal gain"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou use your powers to help others and become a hero.")
        print("Congratulations! You've completed your adventure with a good ending.")
    elif choice == 2:
        print("\nYou use your powers for personal gain and face consequences.")
        print("Your story ends with mixed outcomes.")
        print("Congratulations! You've completed your adventure with an alternative ending.")

def main():
    introduction()
    explore_island()

if __name__ == "__main__":
    main()
