from functools import reduce


def evens_product(L):
    return reduce(lambda x, y: x * y, list(filter(lambda x: x % 2 == 0, L)))


def reverse(L):
    return reduce(lambda x, y: [y] + x, L, [])


def zip_with(f, L1, L2):
    return list(map(lambda x: f(x[0], x[1]), zip(L1, L2)))


def count_if(f, L):
    return len(list(filter(lambda x: f(x), L)))
