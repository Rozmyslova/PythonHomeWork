"""Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?"""

# Вариант 1 - играет человек против бота


def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter the amount = ")
        if not num.isdigit():
            print("This isn`t a correct amount")
            continue
        else:
            return int(num)


print("The player makes the first move. But first, let`s decide on the number of sweets.")
turn = 1
candy = correct_enter()
while candy > 28:
    if turn == 1:
        print("Take no more than 28 candies! ")
        player_choice = correct_enter()
        candy -= player_choice
        print(f"{candy} candies left")
        turn = 2
    else:
        bot_choice = candy % 29
        if bot_choice == 0:
            bot_choice = 28
        candy -= bot_choice
        print(f"Bot takes {bot_choice} candies and {candy} candies on the table")
        turn = 1
    if candy <= 28:
        if turn == 1:
            print(f"{candy} candies left, and Player win - he takes all the candy!")
        else:
            print(f"{candy} candies left, and Bot win - he takes all the candy!")
print("Game over. Thank you for playing! ")
