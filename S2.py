
print('HomeWork 2')
print('')

#14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#*Пример:*

#- 6782 -> 23
#- 0,56 -> 11

print('Задача 14')
print('')
x = input('Введите число ')

def summ(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summ(x)}')
print('')


#15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#*Пример:*

#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задача 15')
print('')
N = int(input('Введите число '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f
    
    print(f, end=" ")
print('')

#16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

print('Задача 16')
print('')
print('Введите число')
i = int(input())
lst = [round((1+1/n)**n, 2) for n in range(1, i+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')
print('')


#17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
#Пример:
#Файл:
#4
#5
#2
#N = 3 => [-3, -2, -1, 0, 1, 2, 3]
#Результат: 1*2*(-1) = -2

print('Задача 17')
print('')

import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")


def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs


n = int(input("Введите число N: "))
numb = [i for i in range(-n, n+1)]
write_file(n)
indx = read_file()
prod = 1
for i in range(len(indx)):
    prod *= numb[indx[i]]
print(f"Результат равен = {prod}")
print('')



#18). Реализуйте алгоритм перемешивания списка.

print('Задача 18')
print('')

import random
lst = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")