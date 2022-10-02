"""Напишите программу для. проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""


def correct_enter():
    correct_ent = False
    while not correct_ent:
        num = input("Enter a value (0 or 1) ")
        if not num.isdigit():
            print("You didn't enter a correct number. Enter a value (0 or 1) ")
            continue
        else:
            num = int(num)
            if num == 0 or num == 1:
                num = bool(num)
                return num
            else:
                print("It isn't correct value. Enter a value (0 or 1) ")
                continue


x = correct_enter()
print(f"x = {x}")
y = correct_enter()
print(f"y = {y}")
z = correct_enter()
print(f"z = {z}")
if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print(f"For x = {x}, y = {y}, z = {z}) the statements is true")
else:
    print(f"For x = {x}, y = {y}, z = {z}) the statements is false")