a = int(input('a: '))

for j in range(a):
    print(j + 1, end='')
    for i in range(j + 1):
        print('*', end='')
    print()