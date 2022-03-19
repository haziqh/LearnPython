
secret_word = "HAZIQ"
word_guessed = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while word_guessed != secret_word.lower() and not out_of_guesses:
    if guess_count < guess_limit:
        word_guessed = input("Guess the word here: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You LOSE! Try again.")
else:
    print("You WIN!")

