# Метод проверки правильности введения длины массива/числа

def correct_enter():
    correct_number = False
    while not correct_number:
        num = input("Enter a length of array/number = ")
        if not num.isdigit():
            print("This isn`t a correct length/number")
            continue
        else:
            return int(num)