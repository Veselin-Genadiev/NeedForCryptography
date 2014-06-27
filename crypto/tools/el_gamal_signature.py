from crypto.tools.utilities import modinv


class ElGamalSignature:
    '''
    This algorithm is used to sign a message. It is based on the dificulty of
    computing discrete logarithm.
    '''

    def __init__(self, modulus, base, private_key, h=lambda x: x):
        if base >= modulus:
            raise ValueError('The base parameter must be less than prime')

        if not 1 < private_key < modulus - 1:
            raise ValueError('Private key should be in range(1, modulus - 1)')

        self.__hash = h
        self.__modulus = modulus
        self.__base = base
        self.__compute = pow(base, private_key, modulus)
        self.__private_key = private_key
        self.__public_key = (modulus, base, self.__compute)

    @property
    def public_key(self):
        return self.__public_key

    def sign(self, message, key):
        if not 1 < key < self.__modulus - 1:
            raise ValueError('Key must be in range (1, modulus - 1)')

        signed = pow(self.__base, key, self.__modulus)
        sign = ((self.__hash(message) - self.__private_key * signed) *
                modinv(key, self.__modulus - 1)) % (self.__modulus - 1)
        return (signed, sign)

    def verify(self, signed, sign):
        return (0 < signed < self.__modulus and 0 < sign < self.__modulus - 1
                and (pow(self.__base, self.__hash(signed), self.__modulus) ==
                     ((pow(self.__compute, signed) * pow(signed, sign))
                      % self.__modulus)))
