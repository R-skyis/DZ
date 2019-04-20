c = 0
def is_prime(a):
    for i in range(2, a // 2 + 1):
        if a % i == 0:

            return False

    return True


a = is_prime(1)

for num in range(2, 100):
    if is_prime(num):
        c += 1
        if c > 10:
            break
        print(num)