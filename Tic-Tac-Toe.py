symbols = ''.join(['_' for i in range(0,9)])
grid = [' '.join(list(symbols[x:x+3])) for x in range(0, len(symbols), 3)]
print('---------')
for row in grid:
    print(f'| {row} |')
print('---------')

repeat_num = 3
starter_list = [1, 2, 3]
col_list = [element for element in starter_list for i in range(repeat_num)]
row_list = [i + 1 for i in starter_list for i in range(repeat_num)]
key_list = tuple(zip(col_list,row_list))
symbols_list = [i for i in symbols]
symbols_dict = {key_list[i]: symbols_list[i] for i in range(len(key_list))}

turn = ['X', 'O']
turn_idx = turn.index('X')
counter = 1
while True:
    try:
        c, r = input().split()
        if int(c) == int() and int(r) == int():
            pass
    except ValueError:
        print('You should enter numbers!')
        continue
    try:
        if symbols_dict[(int(c), int(r))] == '_':
            pass
    except KeyError:
        print('Coordinates should be from 1 to 3!')
        continue

    if symbols_dict[(int(c), int(r))] == '_':
        symbols_dict[(int(c), int(r))] = turn[turn_idx]
        d_string = ''.join(symbols_dict.values())
        grid = [' '.join(list(d_string[x:x + 3])) for x in range(0, len(d_string), 3)]
        print('---------')
        for row in grid:
            print(f'| {row} |')
        print('---------')

        row_1 = set([d_string[i] for i in range(0, 3)])
        row_2 = set([d_string[i] for i in range(3, 6)])
        row_3 = set([d_string[i] for i in range(6, 9)])
        col_1 = set([d_string[i] for i in range(0, len(d_string), 3)])
        col_2 = set([d_string[i] for i in range(1, len(d_string), 3)])
        col_3 = set([d_string[i] for i in range(2, len(d_string), 3)])
        diag_1 = set([d_string[i] for i in range(0, len(d_string), 4)])
        diag_2 = set([d_string[i] for i in range(2, 7, 2)])

        win_list = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]
        for i in win_list:
            if len(i) == 1 and i != [None] and i != {'_'}:
                print(*i, 'wins')
                exit()

    else:
        print('This cell is occupied! Choose another one!')
        continue

    counter += 1
    if counter == 10:
        print('Draw')
        exit()

    turn_idx = 1 - turn_idx