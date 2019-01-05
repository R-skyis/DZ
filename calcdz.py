# не проверено
import math

operation = input('+;-;/;*;sin;cos: ')

if operation == 'sin':
    c = int(input('c: '))
    print(math.sin(c))
    exit()
elif operation == 'cos':
    c = int(input('c: '))
    print(math.cos(c))
    exit()

a = int(input('a: '))
b = int(input('b: '))

if operation == '+':
    print('{} + {} = {}'.format(a, b, a + b))
elif operation == '-':
    print('{} - {} = {}'.format(a, b, a - b))
elif operation == '/':
    print('{} / {} = {}'.format(a, b, a / b))
elif operation == '*':
    print('{} * {} = {}'.format(a, b, a * b))
else:
    print('Нужно ввести знак математической операции (+;-;/;*;sin;cos)')