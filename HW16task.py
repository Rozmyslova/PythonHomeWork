"""Вычислить число π c заданной точностью d
*Пример:*
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$"""

#формула Лейбница

import math
from correct_enter_float import correct_enter_float


d = correct_enter_float()
d = str(d)
d = int(abs(d.find('.') - len(d)))
divider = 1
row_sum = 0
for i in range(1000000):
    if i % 2 == 0:
        row_sum += 4 / divider
    else:
        row_sum -= 4 / divider
    divider += 2
print(row_sum)
pi_accuracy = str(round(row_sum, d))[:-1]
print(pi_accuracy)

