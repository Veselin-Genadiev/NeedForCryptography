import unittest
from symmetric.caeser import Caeser


class CaeserTests(unittest.TestCase):
    def setUp(self):
        self.__data = {23:
                       [('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         'XYZABCDEFGHIJKLMNOPQRSTUVW'),
                        ('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG',
                         'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')],
                       13:
                       [('SYMMETRIC CIPHERS ARE WEAK',
                         'FLZZRGEVP PVCUREF NER JRNX'),
                        ('LIVERPOOL IS THE BEST FOOTBALL CLUB IN THE WORLD',
                         'YVIRECBBY VF GUR ORFG SBBGONYY PYHO VA GUR JBEYQ')]
                       }

    def test_encrypt_decrypt(self):
        for key in self.__data:
            cipher = Caeser(key)
            for pair in self.__data[key]:
                self.assertEqual(cipher.encrypt(pair[0]), pair[1])
                self.assertEqual(cipher.decrypt(pair[1]), pair[0])


if __name__ == '__main__':
    unittest.main()
