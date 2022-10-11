import random
import itertools


def polynom_create(k):
    polynom_coefficient = [random.randint(1,100)]
    [polynom_coefficient.append(random.randint(-10,10)) for i in range(k)]
    print(f"Coefficient of polynom is {polynom_coefficient}")
    polynom_x = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in itertools.zip_longest(polynom_coefficient, polynom_x, range(k, 1, -1), fillvalue = '') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(itertools.chain(*polynom))
    polynom[-1] = ' = 0'
    return polynom
    #"".join(map(str, polynom)).replace(' 1*x',' x')