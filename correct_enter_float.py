
def correct_enter_float():
    correct_num = False
    while not correct_num:
        num = input("Enter the number precision = ")
        try:
            num = float(num)
            return num
        except ValueError:
            print("You didn't enter a correct precision. Enter a number ")