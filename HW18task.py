"""Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]"""

import random


from correct_enter import correct_enter


length = correct_enter()
list_sequence = []
[list_sequence.append(random.randint(1, 10)) for i in range(length)]
print(list_sequence)
unique_list_sequence = []
[unique_list_sequence.append(i) for i in list_sequence if i not in unique_list_sequence]
print(unique_list_sequence)
