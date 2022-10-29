"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

import random


from correct_enter import correct_enter


"""length = correct_enter()
array = []
for i in range(length):
    array.append(random.uniform(1, 50))
    array[i] = round(array[i], 2)
print(array)
max_num = 0
for i in range(length):
    if (array[i] - int(array[i])) > max_num:
        max_num = round(array[i] - int(array[i]), 2)
min_num = 99
for i in range(length):
    if (array[i] - int(array[i])) < min_num:
        min_num = round(array[i] - int(array[i]), 2)
print(f"The difference between the maximum and minimum value is ", round(max_num - min_num, 2))"""


length = correct_enter()
array = []
array = [round(random.uniform(1, 50), 2) for each in range(length)]
print(array)
max_num = [round(array[i] - int(array[i]), 2) for i in range(length)]
min_num = [round(array[i] - int(array[i]), 2) for i in range(length)]
print(f"The difference between the maximum and minimum value is ", round(max(max_num) - min(min_num), 2))
