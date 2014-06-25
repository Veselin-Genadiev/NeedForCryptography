class DiffieHellmanExchange:
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
