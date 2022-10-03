"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11"""


def correct_enter():
    correct_num = False
    while not correct_num:
        num = input("Enter a real number = ")
        num = num.replace(",", ".")
        try:
            num = float(num)
            return num
        except ValueError:
            print("You didn't enter a correct number. Enter a real number ")


number = correct_enter()
if number < 0:
    number = number * (-1)
sum_of_digits = 0
for i in str(number):
    if i != ".":
        sum_of_digits += int(i)
print(sum_of_digits)