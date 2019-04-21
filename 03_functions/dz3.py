c = 0
def is_prime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:

            return False

    return True

a = is_prime(1)

num1 = int(input("От:"))
num2 = int(input("До:"))

def number(n):
    c = 1
    for num in range(num1, num2):
        if is_prime(num):
            c += 1
            if c > n + 1:
                break
            print(num)

n = number(100)
