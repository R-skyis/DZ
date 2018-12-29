a = int(input('а: '))
b = int(input('b: '))
c = int(input('c: '))

x1 = int(((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2))
print('x1 =', x1)
x2 = int(((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2))
print('x2 =', x2)
