import struct


class RC6:
    def __init__(self, key):
        self.state = state = []
        key += "\0" * (4 - len(key) & 3)  # pad key
        L = list(struct.unpack("<%sL" % (len(key) / 4), key))
        state.append(0xb7e15163)

        for i in range(43):
            state.append(_add(state[i], 0x9e3779b9))

        v = max(132, len(L) * 3)

        block1 = block2 = i = j = 0

        for n in range(v):
            block1 = state[i] = _rol(_add(state[i], block1, block2), 3)
            block2 = L[j] = _rol(_add(L[j] + block1 + block2),
                                 _add(block1 + block2))
            i = (i + 1) % len(state)
            j = (j + 1) % len(L)

    def encrypt(self, block):
        state = self.state
        block1, block2, block3, block4 = \
            struct.unpack("<4L", block.ljust(16, '\0'))

        block2 = _add(block2, state[0])
        block4 = _add(block4, state[1])

        for i in range(1, 21):
            t = _rol(_mul(block2, _rol(block2, 1) | 1), 5)
            u = _rol(_mul(block4, _rol(block4, 1) | 1), 5)
            block1 = _add(_rol(block1 ^ t, u), state[2 * i])
            block3 = _add(_rol(block3 ^ u, t), state[2 * i + 1])

            block1, block2, block3, block4 = block2, block3, block4, block1

        block1 = _add(block1, state[42])
        block3 = _add(block3, state[43])

        return struct.pack("<4L", block1, block2, block3, block4)

    def decrypt(self, block):
        state = self.state
        block1, block2, block3, block4 = \
            struct.unpack("<4L", block + "\0" * 16)

        block3 = _add(block3, -state[43])
        block1 = _add(block1, -state[42])

        for i in range(20, 0, -1):
            block1, block2, block3, block4 = block4, block1, block2, block3

            u = _rol(_mul(block4, _add(_rol(block4, 1) | 1)), 5)
            t = _rol(_mul(block2, _add(_rol(block2, 1) | 1)), 5)
            block3 = _ror(_add(block3, -state[2 * i + 1]), t) ^ u
            block1 = _ror(_add(block1, -state[2 * i]), u) ^ t

        block4 = _add(block4, -state[1])
        block2 = _add(block2, -state[0])

        return struct.pack("<4L", block1, block2, block3, block4)


def _add(*args):
    return sum(args) % 4294967296


def _rol(x, n):
    n = 31 & n
    return x << n | 2 ** n - 1 & x >> 32 - n


def _ror(x, y):
    return _rol(x, 32 - (31 & y))


def _mul(a, b):
    return (((a >> 16) * (b & 65535) + (b >> 16) * (a & 65535)) * 65536 +
            (a & 65535) * (b & 65535)) % 4294967296
