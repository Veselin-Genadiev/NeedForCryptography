from symmetric.feistel import Feistel
import unittest


class FeistelTests(unittest.TestCase):
    def setUp(self):
        self.__data = [
            ((2, [{(0, 0): (1, 0), (0, 1): (1, 0),
                   (1, 0): (0, 0), (1, 1): (0, 1)},
                  {(0, 0): (0, 1), (0, 1): (1, 0),
                   (1, 0): (1, 0), (1, 1): (0, 0)},
                  {(0, 0): (1, 1), (0, 1): (0, 0),
                   (1, 0): (0, 1), (1, 1): (1, 0)},
                  {(0, 0): (1, 1), (0, 1): (1, 0),
                   (1, 0): (1, 1), (1, 1): (0, 1)},
                  {(0, 0): (1, 1), (0, 1): (0, 0),
                   (1, 0): (0, 0), (1, 1): (1, 0)},
                  {(0, 0): (1, 1), (0, 1): (1, 1),
                   (1, 0): (0, 1), (1, 1): (1, 0)}],
              '01'
              ), ('0100', '1010')
             )
        ]

    def test_encrypt_decrypt(self):
        for pair in self.__data:
            key = pair[0]
            data = pair[1]
            cipher = Feistel(key[0], key[1], key[2])
            self.assertEqual(cipher.encrypt(data[0]), data[1])
            self.assertEqual(cipher.decrypt(data[1]), data[0])


if(__name__ == '__main__'):
    unittest.main()
