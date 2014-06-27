from crypto.tools.utilities import xgcd, phi


def inv(x, p):
    return xgcd(x, p)[0]


def log(alpha, beta, p):
        totient = phi(p)
        c, j = 1, 0
        B = [beta]
        for i in range(1, c + 1):
            B.append(-1)

        a = []
        for i in range(c):
            a.append(-1)

        while j <= c-1:
                q_j1 = totient ** (j + 1)
                sigma = B[j] ** (totient / q_j1) % p
                for i in range(p):
                    val = alpha ** i % p
                    if sigma == val:
                        a[j] = i
                        break

                if a[j] == -1:
                    raise ValueError("ERROR: Discrete log does not exist")

                z = a[j] * totient ** j
                alpha_inv = inv(alpha, p)
                alpha_inv_z = 1

                for i in range(z):
                    alpha_inv_z = alpha_inv_z * alpha_inv

                B[j+1] = B[j] * alpha_inv_z % p
                j = j + 1

        return a[0]
