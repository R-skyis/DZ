def is_prime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:

            return False

    return True

a = is_prime(1)


def count(n):
    c = 0
    for num in range(2, n * n):
        if is_prime(num):
            c += 1
            if c > n:
                break
            print(num)

n = count(100)
