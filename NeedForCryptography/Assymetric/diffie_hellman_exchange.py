class DiffieHellmanExchange:
    '''
    Diffie-Hellman is ment to be used from lets say Alice and Bob to generate a
    shared key. They arrange two numbers: "modulus" and "base" and use different
    secret keys. Alice and Bob generate public keys and pass them to each other
    to the "exchange" method which generates the shared key.
    '''
    def __init__(self, modulus, base, private_key):
        self.__base = base
        self.__modulus = modulus
        self.__private_key = private_key
        self.__public_key = pow(base, private_key, modulus)

    @property
    def public_key(self):
        return self.__public_key

    def exchange(self, public_key):
        return pow(public_key, self.__private_key, self.__modulus)
