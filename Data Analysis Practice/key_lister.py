
count = 0
keys = []


def add_key_to_list():
    keys.append(user_input)


while True and count < 50:     # 50 item redemption limit per hour

    user_input = str(input('Input key here or type [q] to end: '))

    if user_input == 'q':
        break

    else:
        count += 1
        print(f'Total: {count} item(s)')
        add_key_to_list()
        continue

if count > 0:
    print('---------------------------------------------------------------')
    print(*keys, sep="\n")
    print (f'\nTotal: {count} item(s)')
    print('---------------------------------------------------------------')


