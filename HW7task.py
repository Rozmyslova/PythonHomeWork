"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""


def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter a number = ")
        if not num.isdigit():
            print("This is not a correct enter")
            continue
        else:
            return int(num)


number = correct_enter()
array = []
product = 1
for i in range(number):
    product *= (i + 1)
    i = array.append(product)
print(array)