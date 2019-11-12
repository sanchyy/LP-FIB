def myLength(L):
    return len(L)


def myMaximum(L):
    return max(L)


def average(L):
    sum = 0
    for num in L:
        sum += num
    return float(sum / myLength(L))


def buildPalindrome(L):
    return L[::-1] + L


def remove(L1, L2):
    return [x for x in L1 if x not in L2]


def flatten(L):
    res = []
    for sub_l in L:
        if not isinstance(sub_l, list):
            res.append(sub_l)
        else:
            res += flatten(sub_l)
    return res


def oddsNevens(L):
    return ([x for x in L if x % 2 == 1], [x for x in L if x % 2 == 0])


def primeDivisors(n):
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
    return [x for x in range(2, n+1) if isPrime(x) and n % x == 0]
