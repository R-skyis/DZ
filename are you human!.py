a = 'Земля'
b = 'земля'
e = 'Да'
f = 'да'
c = input("С какой вы планеты?: ")
if c == a or c == b:
    print('Привет Землянин!')
elif c != a or c != b:
    d = input('Ты родился(ась) на планете Земля?: ')
if d == e or d == f:
    print('Привет Землянин!')
else:
    print('Привет рептилойд!')