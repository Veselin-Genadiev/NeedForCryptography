from random import SystemRandom


def phi(n):
    return sum(i for i in range(1, n + 1) if gcd(i, n) == 1)


def chinese_remainder(n, a, lena):
    p = i = prod = 1; sm = 0
    for i in range(lena): prod *= n[i]
    for i in range(lena):
        p = prod / n[i]
        sm += a[i] * mul_inv(p, n[i]) * p
    return sm % prod


def xgcd(a, b):
    x, y, lastx, lasty = 0, 1, 1, 0

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        lastx, x = x, lastx - quotient * x
        lasty, y = y, lasty - quotient * y

    return [lastx, lasty]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % m


def get_random_bit():
    return SystemRandom().getrandbits(1)
