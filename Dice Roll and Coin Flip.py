import random


def menu():
    print("Choose the option you wanna use:\n1- Dice Roll | 2- Coin flip | 3- Exit\n")
    option = int(input())
    if option == 1:
        valid_sides = [4, 6, 8, 10, 12, 20]
        sides = int(input("\nHow many sides?\nValid options: 4, 6, 8, 10, 12, 20\n\n"))
        if sides in valid_sides:
            print("\nDice roll result:", dice_roll(sides), "\n")
            menu()
        else:
            print("\nInvalid option! Try again!\n")
            menu()
    elif option == 2:
        print("\nCoin flip result:", coin_flip(), "\n")
        menu()
    elif option == 3:
        print("\nBye!")
        exit()
    else:
        print("\nInvalid option! Try again!\n")
        menu()


def dice_roll(sides):
    result = random.randint(1, sides)
    return result


def coin_flip():
    result = random.randint(1, 2)
    if result == 1:
        return "Heads"
    else:
        return "Tails"


if __name__ == "__main__":
    print("Welcome!\n")
    menu()
