from symmetric.des3 import DES3
from symmetric.des import DES
import unittest


class DES3ests(unittest.TestCase):
    def setUp(self):
        self.__data = {
            ('alilihuq', 'fantasti', 'selyanin'):
            [('milionerche, ne se podigravai',
              '¦äç÷ba\x1dø1\x0f\x8d\x9c\x84\x82ë¿éB¯^1³ÉéÚ¢*\x1f÷9ð\x01'),
             ('davai davai', '[1\x98>9 BÕp\x8f\x8d6jÍ\x8f5'),
             ('golfo e za nas, troikata za vas',
              'H\x83¼¯Àe\x0fY\x03Yd#9\x94z¼C&\x99ÂkÇ5\x8f\x9aÍJ¤l\x90L\x10'),
             ('Aide minyoroooo', 'T\x04£`ôå÷\x08\x00BÚZ\x16YkS')],
            ('pernikpa', 'radisebe', 'batencee'):
            [('karam golf i sym ot pernik',
              '\x8f\x85êqÝò²éÒ*ÄHWûzéãÌBù\x90)js\x1c[\x0c\x9fÇ?rI'),
             ('izturvahme konqqq',
              "'ê}¨\x01â'ÈPÂ\x92\x92ºVNHÉIjõ\x08\x93>\x8c"),
             ('doko doko', 'í\x17\x05\x1déÌQë7ú9\x87¦\x94\x1f@'),
             ('uebuebuiq', 'ü«(\x9a\x91\x00þýÉIjõ\x08\x93>\x8c'),
             ('skakauec', 'ÝÂ¯\x14Z^Ç\x17\x14Ç\x056Åái\x81'),
             ('uefski, cska = cevski, ueseka',
              '^\\º>\x98\x99\x15~\x97Ä?dÖRQ\x00'
              'ëÐ7ùñx\x98\x82U\x95\x85Cµu\x13|')]
        }

    def test_encrypt_decrypt(self):
        for key in self.__data:
            des3 = DES3(*key)

            for plaintext, ciphertext in self.__data[key]:
                self.assertEqual(des3.encrypt(plaintext), ciphertext)
                self.assertEqual(des3.decrypt(ciphertext), plaintext)

    def test_wrong_key(self):
        key = 'short'
        des = DES()

        with self.assertRaises(ValueError) as ve:
            des.encrypt(key, 'Some stupid message')

        self.assertEqual(ValueError, type(ve.exception))
