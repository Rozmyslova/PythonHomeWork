"""Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

import random


from correct_enter import correct_enter


length = correct_enter()
array = []
for _ in range(length):
    array.append(random.randint(1, 10))
print(array)
sum_of_elements = 0
for i in range(length):
    if i % 2 != 0:
        sum_of_elements += array[i]
print(f"Sum of elements on the odd position is {sum_of_elements}")
