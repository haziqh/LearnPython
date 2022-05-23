import random

computer_wins = 0
user_wins = 0

options = ["r", "p", "s"]

while True:

    print("---------------------------------------------------------------")

    user_input = input("Type [R]ock / [P]aper / [S]cissors or [Q] to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

# Draw
    if user_input == computer_pick:
        print("Draw. Try again.")
        continue

# Wins
    elif user_input == "r" and computer_pick == "s":
        user_wins += 1
        print("You won!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "p" and computer_pick == "r":
        user_wins += 1
        print("You won!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "s" and computer_pick == "p":
        user_wins += 1
        print("You won!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

# Losses
    elif user_input == "r" and computer_pick == "p":
        computer_wins += 1
        print("You lost!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "p" and computer_pick == "s":
        computer_wins += 1
        print("You lost!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

    elif user_input == "s" and computer_pick == "r":
        computer_wins += 1
        print("You lost!")
        print("User wins:", user_wins)
        print("Computer wins:", computer_wins)
        continue

print("You won", user_wins, "time(s).")
print("The computer won", computer_wins, "time(s).")
print("Goodbye!")
