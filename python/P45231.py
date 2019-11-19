def fibs():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a + b

def roots(x):
    a = x
    yield a 
    while True:
        a = 0.5*(a + x/a) 
        yield a

def primes():
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
    res = 2
    yield res
    while True:
        res += 1
        if isPrime(res):
            yield res


def hammings():
    res = 1
    yield res
    while True:
        res += 1
        if res % 2 == 0 or res % 3 == 0 or res % 5 == 0:
            yield res

g4 = hammings()
print([next(g4) for n in range(20)])
