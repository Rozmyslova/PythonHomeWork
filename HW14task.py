"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10"""


from correct_enter import correct_enter


number_dec = correct_enter()
add_number_dec = number_dec
additional_list = []
while add_number_dec != 0:
    remainder = add_number_dec % 2
    additional_list.append(remainder)
    add_number_dec = add_number_dec // 2
length = len(additional_list)
number_bin = []
for i in range(length):
    number_bin.append(additional_list[length - i - 1])
print(f'Decimal number {number_dec} in binary is equal to', ''.join(map(str, number_bin)))

