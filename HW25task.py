"""Дан список чисел. Создайте список, в который попадают числа, описываемые
возрастающую последовательность. Порядок элементов менять нельзя.
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
Входные и выходные данные хранятся в отдельных текстовых файлах."""


def get_new_seq(seq):
    set_new_seq = set()
    for x in range(len(seq)):
        new_seq = [seq[x]]
        for k in seq:
            if k > max(new_seq):
                new_seq.append(k)
            if len(new_seq) >= 2:
                new_seq_tuple = tuple(new_seq)
                set_new_seq.add(new_seq_tuple)
    list_new_seq = list(set_new_seq)
    return list_new_seq


file_ent = open('HW25task_enter', 'r')
sequence_str = file_ent.readline()
sequence = sequence_str.split(", ")
for i in range(len(sequence)):
    sequence[i] = int( sequence[i])
get_new_seq(sequence)

file_ex = open('HW25task_exit', 'w')
for i in range(len(get_new_seq(sequence))):
    print(list(get_new_seq(sequence)[i]))
    file_ex.writelines(str(get_new_seq(sequence)[i]) + "\n")



