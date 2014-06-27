from crypto.tools.utilities import gcd
from math import sqrt
from random import SystemRandom


def is_prime(number):
    return all(number % divisor for divisor in range(2, number))


def filter_divisors(number, numbers):
    for divisor in numbers:
        if divisor % number:
            yield divisor


def primes():
    found = {}
    prime = 2

    while True:
        if prime not in found:
            yield prime
            found[prime * prime] = [prime]
        else:
            for p in found[prime]:
                found.setdefault(p + prime, []).append(p)

            del found[prime]

        prime += 1


def marsenne_number(number):
    return 2 ** number - 1


def is_marsenne_prime(prime):
    s = 4
    marsenne = 2 ** prime - 1

    for _ in range(prime - 2):
        s = (s ** 2 - 2) % marsenne

    return s == 0


def random_prime():
    random = SystemRandom()
    prime_generator = iter(primes())
    prime_number = next(prime_generator)

    for _ in range(random.randrange(42)):
        prime_number = next(prime_generator)

    while not is_marsenne_prime(prime_number):
        prime_number = next(prime_generator)

    return marsenne_number(prime_number)


def random_prime_pair():
    first = random_prime()
    second = random_prime()

    while first == second:
        second = random_prime()

    return (first, second)


def factor_primes(number):
    return [factor for factor in range(2, number) if is_prime(factor)]


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

    for l, r in pairs:
        if l != r:
            factor = gcd(l - r, number)
            if(factor > 1):
                factors.append(factor)

    return factors
