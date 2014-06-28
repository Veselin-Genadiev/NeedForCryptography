from tools.el_gamal_signature import ElGamalSignature
import unittest


class ElGamalSignatureTests(unittest.TestCase):
    def setUp(self):
        self.__data = {
            (17, 1, 15): [
                ((1234, 5), (1, 7)),
                ((5324, 7), (1, 11)),
                ((74532, 3), (1, 7)),
                ((6685, 9), (1, 14))
            ],
            (31, 1, 18): [
                ((9969, 7), (1, 3)),
                ((42, 13), (1, 18))
            ]
        }

    def test_sign_verify(self):
        for key in self.__data:
            signature = ElGamalSignature(*key)
            for pair in self.__data[key]:
                self.assertEqual(signature.sign(*pair[0]), pair[1])
                self.assertTrue(signature.verify(*pair[1]))

    def test_sign_with_invalid_key(self):
        signature = ElGamalSignature(31, 1, 18)
        with self.assertRaises(ValueError) as ve:
            signature.sign(1231255, 5)

        self.assertEqual(ValueError, type(ve.exception))
        self.assertRaises(ValueError, signature.sign, 12312, 32)
        self.assertRaises(ValueError, ElGamalSignature, 31, 32, 18)
