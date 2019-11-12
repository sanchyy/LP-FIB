def absValue(x):
    return -x if x < 0 else x


def power(x, p):
    return x ** p


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-1) + slowFib(n-2)


def quickFib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

