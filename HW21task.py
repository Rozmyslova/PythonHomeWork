"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

text_line = input("Enter a text with 'абв' = ")
find_text = "абв"
new_text = [i for i in text_line.split() if find_text not in i]
print(f'Result is =  {" ".join(new_text)}')

