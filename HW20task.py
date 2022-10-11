"""Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными.
Степени многочленов могут отличаться."""

import random
import itertools
from correct_enter import correct_enter
from polynom_create import polynom_create


"""def sum_polynom(pol1, pol2):
    add_pol = [0] * (max)
    min_length = min(len(pol1), len(pol2))
    for i in range(min_length):
        if pol1[i][1] == pol2[i][1]:
            pol = pol1[i][0] + pol2[i][0]
            if pol != 0:
                sum_pol.append(pol, pol1[i][1])
        if pol1[i][1] != pol2[i][1]:
            sum_pol.append(pol2[i])
            sum_pol.append(pol1[i])
    return sum_pol"""


polynom_degree1 = correct_enter()
polynom1 = polynom_create(polynom_degree1)
print(polynom1)
"""with open('Pln1_20task.txt', 'w') as pln1:
    pln1.write(polynom1)"""

polynom_degree2 = correct_enter()
polynom2 = polynom_create(polynom_degree2)
print(polynom2)
"""with open('Pln2_20task.txt', 'w') as pln2:
    pln2.write(polynom2)"""
#polynom_res = sum_polynom(polynom1, polynom2)

