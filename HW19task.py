"""Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
*Пример:*
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""

import random
import itertools
from correct_enter import correct_enter


def polynom_create(k):
    polynom_coefficient = [random.randint(1,100)]
    [polynom_coefficient.append(random.randint(0,100)) for i in range(k)]
    print(f"Coefficient of polynom is {polynom_coefficient}")
    polynom_x = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(polynom_coefficient, polynom_x, range(k, 1, -1), fillvalue = '') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x',' x')


polynom_degree = correct_enter()
polynom = polynom_create(polynom_degree)
print(polynom)
with open('Polynom1.txt', 'w') as pln:
    pln.write(polynom)
