from Symmetric.Playfair import Playfair
import unittest


class PlayfairTests(unittest.TestCase):
    def setUp(self):
        self.data = {'qazwsxedcrfvtgbyhnujmiklo':
                     [('qw er ty', 'as dx fn'),
                      ('dw ay ne th er oc kj oh ns on',
                       'cz qh hd vn dx lr on ij jz kj'),
                      ('ih at em at hs', 'ai zv xi zv ja')],
                     'qazwsxedcrfvtgby': [('fa tb ea rs', 'rz gy xz cx'),
                                          ('de ar ce as er',
                                           'sd xg fs qx xf')]
                     }

    def test_encrypt_decrypt(self):
        for key in self.data:
            cipher = Playfair(key)
            for pair in self.data[key]:
                self.assertEqual(cipher.encrypt(pair[0]), pair[1])
                self.assertEqual(cipher.decrypt(pair[1]), pair[0])

    '''
    Raises error for text with odd length
    '''
    def test_invalid_text(self):
        key = 'qazwsxedc'
        text = 'qwe'
        cipher = Playfair(key)
        self.assertRaises(ValueError, cipher.encrypt, text)

if __name__ == '__main__':
    unittest.main()
