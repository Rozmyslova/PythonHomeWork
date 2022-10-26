#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def compression(line):
    compression_line = ""
    i = 0
    while i < len(line):
        count = 1
        while i + 1 < len(line) and line[i] == line[i + 1]:
            count += 1
            i += 1
            if count >= 9:
                break
        compression_line += str(count) + line[i]
        i += 1
    return compression_line


def recovery(x):
    num = []
    letters = []
    temp = list(x)
    for i in range(0, len(temp) - 1, 2):
        num.append(temp[i])
        letters.append((temp[i+1]))
    recovering_line = ""
    for i in range(len(letters)):
        recovering_line += letters[i] * int(num[i])
    return recovering_line


f1 = open('HW24task_enter_string', 'r')

enter_str = f1.readline()
print(enter_str)
line = compression(enter_str)
print(line)
with open('HW24task_compression', 'w') as f2:
    f2.write(line)
print(recovery(line))
with open('HW24task_recov', 'w') as f3:
    f3.write(recovery(line))
