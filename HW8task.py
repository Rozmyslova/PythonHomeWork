"""Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072"""


def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter a number = ")
        if not num.isdigit():
            print("This isn`t a correct enter")
            continue
        else:
            return int(num)


number = correct_enter()
array = []
sum_of_array = 0
for i in range(number):
    i += 1
    i = (1 + 1 / i) ** i
    sum_of_array += i
    i = array.append((1+1/i)**i)
print(round(sum_of_array, 3))
