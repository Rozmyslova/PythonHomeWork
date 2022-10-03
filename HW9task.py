"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры."""

from random import randint


def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter a number = ")
        if not num.isdigit():
            print("This isn`t a correct number")
            continue
        else:
            return int(num)


def correct_n():
    n = correct_enter()
    correct = False
    while not correct:
        if n == 0:
            print("Number mustn`t be 0")
            n = correct_enter()
        else:
            return n


def correct_position(num):
    correct_number = False
    while not correct_number:
        pos = correct_enter()
        if (pos >= num) or (pos < 0):
            print("It isn`t a correct position")
            continue
        else:
            return pos


number = correct_n()
array = []
for _ in range(number):
    array.append(randint(-number, number))
print(array)
print("Enter a number of position A (0 <= A < N) = ")
a = correct_position(number)
print("Enter a number of position B (0 <= B < N) = ")
b = correct_position(number)
product = array[a] * array[b]
print(product)
