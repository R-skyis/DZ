a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a == b == c:
    a = a + 5
    b = b + 5
    c = c + 5
    print('a + 5 =', a, 'b + 5 =', b, 'c + 5 =', c)
elif a == b:
    a = a + 5
    b = b + 5
    c = c + 5
    print('a + 5 =', a, 'b + 5 =', b, 'c + 5 =', c)
elif a == c:
    a = a + 5
    b = b + 5
    c = c + 5
    print('a + 5 =', a, 'b + 5 =', b, 'c + 5 =', c)
elif b == c:
    a = a + 5
    b = b + 5
    c = c + 5
    print('a + 5 =', a, 'b + 5 =', b, 'c + 5 =', c)
else:
    print('Равных нет!')
