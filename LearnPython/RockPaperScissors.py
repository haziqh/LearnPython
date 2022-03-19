import random

computer_wins = 0
user_wins = 0

options = ["r", "p", "s"]

while True:
    user_input = input("Type [R]ock / [P]aper / [S]cissors or [Q] to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "s" and computer_pick == "p":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")


print("Goodbye!")
