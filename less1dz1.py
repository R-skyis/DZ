# (a + b - f / a) + f * a * a - (a + b) Числа а, b, f вводятся с клавиатуры.
a = int(input('Введите A: '))
b = int(input('Введите B: '))
f = int(input('Введите F: '))
c = int(a + b - f / a) + f * a * a - (a + b)
print('Результат:', c)
