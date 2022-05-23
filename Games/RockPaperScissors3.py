import random

user_wins = 0
computer_wins = 0
draw_count = 0
game_count = 0
win_percentage = 0
computer_win_percentage = 0
draw_percentage = 0

user_options = ['r', 'p', 's']
options = ['Rock', 'Paper', 'Scissors']

while True:

    print('---------------------------------------------------------------')

    user_input = input('Type [R]ock / [P]aper / [S]cissors or [Q] to quit: ').lower()

    if user_input == 'q':
        break

    if user_input not in user_options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print('\nComputer picked', computer_pick + '.')

# Draw
    if user_input == 'r' and computer_pick == 'Rock':
        print('Draw. Try again.')
        draw_count += 1
        game_count += 1
        continue

    elif user_input == 'p' and computer_pick == 'Paper':
        print('Draw. Try again.')
        draw_count += 1
        game_count += 1
        continue

    elif user_input == 's' and computer_pick == 'Scissors':
        print('Draw. Try again.')
        draw_count += 1
        game_count += 1
        continue

# Wins
    elif user_input == 'r' and computer_pick == 'Scissors':
        user_wins += 1
        game_count += 1
        print('You won!')
        print('\nUser wins:', user_wins)
        print('Computer wins:', computer_wins)
        print('Games played:', game_count)
        continue

    elif user_input == 'p' and computer_pick == 'Rock':
        user_wins += 1
        game_count += 1
        print('You won!')
        print('\nUser wins:', user_wins)
        print('Computer wins:', computer_wins)
        print('Games played:', game_count)
        continue

    elif user_input == 's' and computer_pick == 'Paper':
        user_wins += 1
        game_count += 1
        print('You won!')
        print('\nUser wins:', user_wins)
        print('Computer wins:', computer_wins)
        print('Games played:', game_count)
        continue

# Losses
    else:
        computer_wins += 1
        game_count += 1
        print('You lost!')
        print('\nUser wins:', user_wins)
        print('Computer wins:', computer_wins)
        print('Games played:', game_count)
        continue

if user_wins > 0:
    win_percentage = (user_wins / game_count) * 100
    computer_win_percentage = (computer_wins / game_count) * 100
    draw_percentage = (draw_count / game_count) * 100



print(f'\nYou won {user_wins} ({round(win_percentage, 2)}%) time(s).')
print(f'The computer won {computer_wins} ({round(computer_win_percentage, 2)}%) time(s).')
print(f'Number of draw(s): {draw_count} ({round(draw_percentage, 2)}%) time(s).')
print('Goodbye!')






#print(f'Number of draw(s):' {draw_count} ({draw_percentage}%) time(s).')
#print('The computer won', computer_wins, '(' + str(round(computer_win_percentage, 2)) + '%' + ')', 'time(s).')
#print('Number of draw(s):', draw_count, '(' + str(round(draw_percentage, 2)) + '%' + ')',)
