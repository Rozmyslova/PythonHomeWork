"""Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет"""


def correct_enter():
    correct_enter = False
    while not correct_enter:
        day_of_a_week = input("Enter a number in range of 1 to 7 ")
        if not day_of_a_week.isdigit():
            print("This is not a correct enter")
            continue
        else:
            day_of_a_week = int(day_of_a_week)
            if day_of_a_week < 1 or day_of_a_week > 7:
                print("There is no such day of the week")
                continue
            else:
                return day_of_a_week


day_of_a_week = correct_enter()
if day_of_a_week == 6 or day_of_a_week == 7:
    print("This is a day off")
else:
    print("This is a weekday")