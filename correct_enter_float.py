
def correct_enter_float():
    correct_num = False
    while not correct_num:
        num = input("Enter the number precision in range (10**(-10) <= num <= 10**(-1))= ")
        if num.isdigit():
            print("This isn`t a correct length/number. Enter a float number ")
            continue
        try:
            num = float(num)
            if 10**(-10) <= num <= 10**(-1):
                return num
            else:
                print("You didn't enter a correct precision. Enter other number ")
        except ValueError:
            print("You didn't enter a correct precision. Enter a number ")