"""Напишите программу, которая по заданному номеру четверти, показывает
диапазон возможных координат точек в этой четверти (x и y)."""


def correct_enter():
    correct_quarter = False
    while not correct_quarter:
        quarter = input("Enter a number of quarter (1,2,3,4) ")
        if not quarter.isdigit():
            print("You didn't enter a correct number. Enter a number (1, 2, 3 or 4) ")
            continue
        else:
            quarter = int(quarter)
            if quarter < 1 or quarter > 4:
                print("It isn't correct quarter. Enter a number (1, 2, 3 or 4) ")
            else:
                return quarter


quarter = correct_enter()
if quarter == 1:
    print("A range of X_coordinate (0; + infinite)", "A range of Y_coordinate (0; + infinite)", sep="\n")
elif quarter == 2:
    print("A range of X_coordinate (- infinite; 0)", "A range of Y_coordinate (0; + infinite)", sep="\n")
elif quarter == 3:
    print("A range of X_coordinate (- infinite; 0)", "A range of Y_coordinate (- infinite; 0)", sep="\n")
else:
    print("A range of X_coordinate (0; + infinite)", "A range of Y_coordinate (- infinite; 0)", sep="\n")
