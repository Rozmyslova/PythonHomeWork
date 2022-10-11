"""Задайте натуральное число N. Напишите программу, которая составит
список простых множителей числа N.
*Пример*
- при N=236     ->        [2, 2, 59]"""

from correct_enter import correct_enter


number = correct_enter()
list_all_multi = []
i = 2
while i <= number:
    if number % i == 0:
        list_all_multi.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"All prime numbers of {number} is {list_all_multi}")
# Перечень уникальных простых множителей
print(f"Unique prime numbers of {number} is {set(list_all_multi)}")

