# Создайте программу для игры в "Крестики-нолики"
# Второй вариант - играет человек с ботом

import random


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


def turn_bot(game_field, player_sym, bot_sym, win_combination):
    bot_choice = False
    new_combination = list()
    while not bot_choice:
        for elements in win_combination:
            if game_field[elements[0]] in [player_sym, bot_sym] and game_field[elements[1]] in [player_sym, bot_sym] \
                    and game_field[elements[2]] in [player_sym, bot_sym]:
                continue
            new_combination.append(elements)
        for elements in new_combination:
            buf = [i for i in elements if game_field[i] == bot_sym]
            if len(buf) == 2:
                game_field[elements[0]] = bot_sym
                game_field[elements[1]] = bot_sym
                game_field[elements[2]] = bot_sym
                return True
        for elements in new_combination:
            buf = [i for i in elements if game_field[i] == player_sym]
            if len(buf) == 2:
                for i in elements:
                    if field[i] != player_sym:
                        game_field[i] = bot_symbol
                        return True

        not_used_cells = [i for i in game_field if i not in ["X", "O"]]
        cell = random.choice(not_used_cells)
        field[cell - 1] = bot_sym
        return False


def correct_win(game_field):
    for elements in winner_combination:
        if game_field[elements[0]] == game_field[elements[1]] == game_field[elements[2]]:
            return True
    return False


field = list(range(1, 10))
fill_game_field(field)
print("The player puts X, the bot player puts O. The player makes the first move. Let's start a game")
winner_combination = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
turn = 1
player_symbol = "X"
while turn < 10:
    if turn % 2 != 0:
        print("Player's turn")
        player = "Player"
        correct_enter(player_symbol)
        fill_game_field(field)
    else:
        print("Bot's turn")
        player = "Bot"
        bot_symbol = "O"
        if turn == 4:
            print("hello")
        turn_bot(field, player_symbol, bot_symbol, winner_combination)
        fill_game_field(field)
    if turn > 4:
        if correct_win(field):
            print(f"{player} is winner")
            break
        elif turn == 9:
            print("Friendship won")
    turn += 1
