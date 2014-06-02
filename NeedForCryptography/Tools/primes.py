import itertools
from math import sqrt


def is_prime(number):
    return all(number % divisor for divisor in range(2, number))


def filter_divisors(number, numbers):
    for divisor in numbers:
        if divisor % number:
            yield divisor


def primes():
    candidates = itertools.count(2)

    while True:
        prime = next(candidates)
        candidates = filter_divisors(prime, candidates)
        yield prime


def fermat_number(prime):
    if not is_prime(prime):
        raise ValueError('Number is not prime')

    return 2 ** (2 ** prime) + 1


def marsene_prime(prime):
    if not is_prime(prime):
        raise ValueError('Number is not prime')

    return 2 ** prime - 1


def gcd(a, b):
    if a % b == 0:
        return a

    return gcd(b, a % b)


def dixon_factor(number):
    base = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    start = int(sqrt(number))
    pairs = []
    factors = []

    for i in range(start, number):
        for j in range(len(base)):
            lhs = i**2 % number
            rhs = base[j]**2 % number

            if lhs == rhs:
                pairs.append([i, base[j]])

    for i in range(len(pairs)):
        factor = gcd(pairs[i][0] - pairs[i][1], number)

        if(factor != 1):
            factors.append(factor)

    return factors
