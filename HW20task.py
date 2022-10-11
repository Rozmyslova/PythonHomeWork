"""Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
Коэффициенты могут быть как положительными, так и отрицательными.
Степени многочленов могут отличаться."""

import random
import itertools
from correct_enter import correct_enter
from polynom_create import polynom_coef
from polynom_create import polynom_create

polynom_degree1 = correct_enter()
polynom_coefficient1 = polynom_coef(polynom_degree1)
polynom1 = polynom_create(polynom_degree1, polynom_coefficient1)
print(polynom1)
with open('Pln1_20task.txt', 'w') as pln1:
    pln1.write(polynom1)

polynom_degree2 = correct_enter()
polynom_coefficient2 = polynom_coef(polynom_degree2)
polynom2 = polynom_create(polynom_degree2, polynom_coefficient2)
print(polynom2)
with open('Pln2_20task.txt', 'w') as pln2:
    pln2.write(polynom2)

polynom1_rev = list(reversed(polynom_coefficient1))
polynom2_rev = list(reversed(polynom_coefficient2))
polynom1_rev.extend([0, ] * (len(polynom2_rev) - len(polynom1_rev)))
polynom2_rev.extend([0, ] * (len(polynom1_rev) - len(polynom2_rev)))
polynom_coef_rev = list(map(sum, zip(polynom1_rev, polynom2_rev)))
polynom_coef = list(reversed(polynom_coef_rev))

if polynom_degree1 > polynom_degree2:
    polynom_degree = polynom_degree1
else:
    polynom_degree = polynom_degree2

polynom_res = polynom_create(polynom_degree, polynom_coef)
print(polynom_res)
with open('Pln_res_20task.txt', 'w') as pln_res:
    pln_res.write(polynom_res)