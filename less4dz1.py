def is_prime(a):
    if a % 2 == 0:
        return('false')
    else:
        return('true')
a = int(input())

print(is_prime(a))
