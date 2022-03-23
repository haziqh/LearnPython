
game_count = 0
keys = []


def add_key_to_list():
    keys.append(user_input)


while True and game_count < 50:     # Steam has a 50 game redemption limit per hour

    user_input = str(input('Input key here or type [q] to end: '))

    if user_input == 'q':
        break

    else:
        game_count += 1
        print(f'Total: {game_count} game(s)')
        add_key_to_list()
        continue

if game_count > 0:
    print('---------------------------------------------------------------')
    print(*keys, sep="\n")
    print (f'\nTotal: {game_count} game(s)')
    print('---------------------------------------------------------------')


