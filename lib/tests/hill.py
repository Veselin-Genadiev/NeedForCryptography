from symmetric.hill import Hill
import unittest


class HillTests(unittest.TestCase):
    def setUp(self):
        self.__data = []

    def test_encrypt_decrypt(self):
        for key, pairs in self.__data:
            cipher = Hill(key)
            for pair in pairs:
                self.assertEqual(cipher.encrypt(pair[0]), pair[1])
                self.assertEqual(cipher.decrypt(pair[1]), pair[0])

    def test_invalid_text(self):
        key = [[3, 3], [2, 5]]
        text = 'HEY'
        cipher = Hill(key)
        self.assertRaises(ValueError, cipher.encrypt, text)
