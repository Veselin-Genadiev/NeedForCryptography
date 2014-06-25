def log(base, value, modulo):
    for power in range(0, modulo + 1):
        if value == base ** power % modulo:
            return power

    raise ValueError('log{}({}) does not have discrete logarithm in {}'
                     .format(base, value, modulo))
