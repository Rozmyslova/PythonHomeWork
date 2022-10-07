"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """


from correct_enter import correct_enter

number = correct_enter()
negafibonacci = [0, 1]
fib1 = 0
fib2 = 1
for i in range(-1, -number, -1):
    fib1, fib2 = fib2, fib1 - fib2
    negafibonacci.append(fib2)
fibonacci = []
for i in range(number + 1):
    fibonacci.append(negafibonacci[number - i])
fibonacci.append(1)
fibonacci.append(1)
fib1 = fib2 = 1
for i in range(2, number):
    fib1, fib2 = fib2, fib1 + fib2
    fibonacci.append(fib2)
print(fibonacci)









