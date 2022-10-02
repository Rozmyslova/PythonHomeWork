"""Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21"""


def correct_enter():
    correct_num = False
    while not correct_num:
        num = input("Enter the coordinate = ")
        try:
            num = float(num)
            return num
        except ValueError:
            print("You didn't enter a correct coordinate. Enter a number ")


print("Enter coordinate of point A (x, y)")
coordinate_x_A = correct_enter()
print(f"Coordinate X of point A = {coordinate_x_A}")
coordinate_y_A = correct_enter()
print(f"Coordinate Y of point A = {coordinate_y_A}")
print("Enter coordinate of point B (x, y)")
coordinate_x_B = correct_enter()
print(f"Coordinate X of point B = {coordinate_x_B}")
coordinate_y_B = correct_enter()
print(f"Coordinate Y of point B = {coordinate_y_B}")
length_AB = ((coordinate_x_B - coordinate_x_A)**2 + (coordinate_y_B - coordinate_y_A)**2)**(0.5)
result_length_AB = str(round(length_AB, 3))[:-1]
print(f"Length between 2 points is {result_length_AB}")