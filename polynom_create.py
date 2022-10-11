import random
import itertools


def polynom_coef(k):
    polynom_coefficient = [random.randint(1, 100)]
    [polynom_coefficient.append(random.randint(-10, 10)) for i in range(k)]
    return polynom_coefficient


def polynom_create(k, pol_coef):
    polynom_x = ['*x^'] * (k - 1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(pol_coef, polynom_x, range(k, 1, -1), fillvalue='') if
               a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x')
