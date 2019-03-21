a = int(input('Введите число:'))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
result = factorial(a)
print(result)
