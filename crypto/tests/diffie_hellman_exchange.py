from asymmetric.diffie_hellman_exchange import DiffieHellmanExchange
import unittest


class DiffieHellmanExchangeTests(unittest.TestCase):
    def setUp(self):
        self.__data = [
            ((16543, 24537), (6543, 6777123)),
            ((212313, 53455), (7456, 546715)),
            ((635, 3563), (1231, 654363)),
            ((175672, 7765), (12312, 63466))
        ]

    def test_exchange(self):
        for key, pair in self.__data:
            alice = DiffieHellmanExchange(*key, private_key=pair[0])
            bob = DiffieHellmanExchange(*key, private_key=pair[1])
            self.assertEqual(alice.exchange(bob.public_key),
                             bob.exchange(alice.public_key))
