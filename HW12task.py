"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

import random


from correct_enter import correct_enter


"""length = correct_enter()
array = []
for _ in range(length):
    (array.append(random.randint(1, 10)))
print(array)
if length % 2 == 0:
    new_length = int(length / 2)
else:
    new_length = int(length / 2) + 1
new_array = []
for i in range(new_length):
    new_array.append(array[i] * array[length - i - 1])
print(new_array)"""

length = correct_enter()
array = [random.randint(1, 10) for each in range(length)]
print(array)
new_length = length // 2 if length % 2 == 0 else length // 2 + 1
rew_array = array[::-1]
rew_array = rew_array[:new_length]
array = array[:length]
new_array = list(map(lambda x: x[0] * x[1], zip(rew_array, array)))
print(new_array)
