# keys = ['BQB2E-5VAQG-Q99C7', 'B6HIL-2JKJ5-2W2RD', 'BQAHY-YF572-E98EW', 'ALYBG-64EBK-RQYY0', 'A5CTV-JWIX6-C8M5K', 'BF6H0-ZEXK7-6QT08', 'BB0N6-ZH59J-LKQJ4', 'AHIR2-DGQXK-Z9NXC', 'AAZXJ-J0XBD-DVIJR', 'ADEZC-Y9LD4-THMDV', 'AFBKY-DPYGL-ERGP6', 'BECMG-A3BF4-JTPML', 'BP0GX-NZMTR-VMYQK', 'ATAZA-75KW6-YCQPN', 'AQZ36-FPQIZ-MATEN', 'BBN2J-4HPFJ-5L4XL', 'ANQG7-QH2IW-B6C5Y', 'AFXMV-GFZKP-5DFV7', 'BFZ5I-N05DZ-HLE6P', 'B0LJQ-Z6H74-L6IET', 'AW0T3-AFHPH-ZDKNN', 'AWTD9-6GJC9-GNZ8J', 'B6QKJ-WVY2P-YK0VN', 'AZIDJ-2FBQP-PTZIE', 'AWN8Y-YG0I8-XB938', 'AENEY-GDVQ2-PTHLG', 'AJ4YX-JT0AN-2IAG3', 'ADACD-QXJCX-VN40L', 'AAF3V-BTHBX-33MQQ', 'KKLC6-ZVN0K-XHL0P']
# print("\n" + str(len(keys)))
# while len(keys) < maxLength:

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


