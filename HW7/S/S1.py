# Вывести квадрат числа
number = int(input('Input number: \n'))
print('Квадрат числа {1} равен {0} ' .format(number, number**2), end='/// ')
print(f'Квадрат числа {number} равен {number**2}')
print('Квадрат числа', number, 'равен', number**2)

#проверить, являетсяя ли число квадратом другого
a = int(input('A='))
b = int(input('B='))
print(f'{a}, {b} ->', end=' ')
if a == b**2 or b == a**2:
    print('да')
else:
    print('нет')