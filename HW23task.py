# Создайте программу для игры в "Крестики-нолики"
# Первый вариант - играют два человека

def fill_game_field(game_field):
    for i in range(3):
        print(" ", game_field[i * 3 + 0], "|", game_field[i * 3 + 1], "|", game_field[i * 3 + 2])
        if i == 2:
            break
        print(" ", "_" * 10)


def correct_enter(symbol):
    correct_cell = False
    while not correct_cell:
        cell = input(f"Enter the cell number in the field (1 to 9) for {symbol} = ")
        if not cell.isdigit():
            print("Entered not a number")
            continue
        else:
            cell = int(cell)
            if 0 < cell < 10:
                if str(field[cell - 1]) in "XO":
                    print("This cell isn't selectable. Choose another cell")
                    continue
                else:
                    field[cell - 1] = player_symbol
                    correct_cell = True
            else:
                print("This isn`t a correct cell. ")


def correct_win(game_field):
    winner_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for elements in winner_combination:
        if game_field[elements[0]] == game_field[elements[1]] == game_field[elements[2]]:
            return True
    return False


field = list(range(1, 10))
fill_game_field(field)
print("First player puts X, second player puts O. Let's start a game")
turn = 1
while turn < 10:
    if turn % 2 != 0:
        print("First player's turn")
        player = "First player"
        player_symbol = "X"
        correct_enter(player_symbol)
        fill_game_field(field)
    else:
        print("Second player's turn")
        player = "Second player"
        player_symbol = "O"
        correct_enter(player_symbol)
        fill_game_field(field)
    if turn > 4:
        if correct_win(field):
            print(f"{player} is winner")
            break
        elif turn == 9:
            print("Friendship won")
    turn += 1
