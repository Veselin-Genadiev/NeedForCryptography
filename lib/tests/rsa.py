from asymmetric.rsa import RSA
import unittest


class RSATests(unittest.TestCase):
    def setUp(self):
        self.__data = {
            (61, 53, 17): [
                ('You will never walk alone',
                 'c\u0889\u0870߈ѓ౫˩˩߈\u08bbԡ\u0a12ԡ६߈ѓ٠˩ʲ߈٠˩\u0889\u08bbԡ'),
                ('Me no speak americano',
                 'ళԡ߈\u08bb\u0889߈ӎɤԡ٠ʲ߈٠\u08dfԡ६౫ę٠\u08bb\u0889'),
                ('Spam spam spam', '\u0a78ɤ٠\u08df߈ӎɤ٠\u08df߈ӎɤ٠\u08df'),
                ('I dont give a shit',
                 '\u05ce߈ۭ\u0889\u08bbʹ߈୫౫\u0a12ԡ߈٠߈ӎ\u087a౫ʹ'),
                ('Viva las vegas', 'ݲ౫\u0a12٠߈˩٠ӎ߈\u0a12ԡ୫٠ӎ')
            ]
        }

    def test_encrypt_decrypt(self):
        for key in self.__data:
            cipher = RSA(*key)
            for pair in self.__data[key]:
                self.assertEqual(RSA.encrypt(cipher.public_key, pair[0]),
                                 pair[1])
                self.assertEqual(cipher.decrypt(pair[1]), pair[0])

    def test_public_key_not_modulus_coprime(self):
        with self.assertRaises(ValueError) as ve:
            RSA(61, 53, 33)

        self.assertEqual(ValueError, type(ve.exception))
