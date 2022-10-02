"""Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3"""


def correct_enter():
    correct_num = False
    while not correct_num:
        num = input("Enter the coordinate = ")
        try:
            num = float(num)
            return num
        except ValueError:
            print("You didn't enter a correct coordinate. Enter a number ")


coordinate_x = correct_enter()
print(f"coordinate_x = {coordinate_x}")
coordinate_y = correct_enter()
print(f"coordinate_y = {coordinate_y}")
if coordinate_x > 0 and coordinate_y > 0:
    print(f"Point with coordinates {coordinate_x}, {coordinate_y} is located in 1 quarter")
elif coordinate_x < 0 and coordinate_y > 0:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is located in 2 quarter")
elif coordinate_x < 0 and coordinate_y < 0:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is located in 3 quarter")
elif coordinate_x > 0 and coordinate_y < 0:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is located in 4 quarter")
elif coordinate_x == 0 and coordinate_y != 0:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is located on the Y axis")
elif coordinate_x != 0 and coordinate_y == 0:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is located on the X axis")
else:
    print(f"Point with coordinates ({coordinate_x}, {coordinate_y}) is origin")