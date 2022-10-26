"""Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?"""

# Вариант 1 - играют 2 человека


def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter the amount = ")
        if not num.isdigit():
            print("This isn`t a correct amount")
            continue
        else:
            return int(num)


print("Two people are playing. They take turns taking candy (any number from 1 to 28). "
      "\n The winner is the one who took the candy last. But first, let`s decide on the number of sweets.")
turn = 1
candy = correct_enter()
while candy > 28:
    if turn == 1:
        player = "First player"
        print(f"{player},take no more than 28 candies! ")
        player_choice = correct_enter()
        candy -= player_choice
        print(f"{candy} candies left")
        turn = 2
    else:
        player = "Second player"
        print(f"{player},take no more than 28 candies! ")
        player_choice = correct_enter()
        candy -= player_choice
        print(f"{candy} candies left")
        turn = 1
    if candy <= 28:
        if player == "First player":
            player = "Second player"
        else:
            player = "First player"
        print(f"{candy} candies left, and {player} win - he takes all the candy!")
print("Game over. Thank you for playing! ")
