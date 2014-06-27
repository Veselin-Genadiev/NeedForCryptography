from crypto.tools.utilities import modinv


class RSA:
    '''
    The most common used cipher. RSA relies on the fact that factorizing a
    number in primes is a slow operation. To use the cipher please pass two
    large primes and a number which is coprime to phi(the product of the primes)
    where phi is the Oyler's function. Message for encrypt and decrypt must be
    plain text. Static method encrypt must recieve a public key as an argument.
    '''
    def __init__(self, first_prime, second_prime, phi_coprime):
        self.__modulus = first_prime * second_prime
        phi = (first_prime - 1) * (second_prime - 1)
        self.__phi_coprime = phi_coprime
        self.__reverse_phi_coprime = modinv(phi_coprime, phi)

    @staticmethod
    def encrypt(public_key, message):
        modulus, phi_coprime = public_key
        cipher = [pow(ord(char), phi_coprime, modulus) for char in message]
        return ''.join(chr(index) for index in cipher)

    def decrypt(self, message):
        cipher = [pow(ord(char), self.__reverse_phi_coprime,
                      self.__modulus) for char in message]
        return ''.join(chr(index) for index in cipher)

    @property
    def public_key(self):
        return (self.__modulus, self.__phi_coprime)
