"""Реализуйте алгоритм перемешивания списка."""
import random

array = ["World", "3", "Moscow", "-4.123", "student", "mark", "reason", "1000"]
length = len(array)
new_array = array[:]
for i in range(length):
    random_index = random.randint(0, length - 1)
    temp = new_array[i]
    new_array[i] = new_array[random_index]
    new_array[random_index] = temp
print(array)
print(new_array)
