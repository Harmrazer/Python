print('HomeWork 5.1')
print('')

#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print('Задача 1')
print('')


txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')

