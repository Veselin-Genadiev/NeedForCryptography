import crypto.symmetric.des as DES


class DES3:
    des = DES.DES()

    def __init__(self, key1, key2, key3):
        if not len(key1) == len(key2) == len(key3) == 8:
            raise ValueError('Keys should be 8 bytes long')

        self.__keys = (key1, key2, key3)

    def encrypt(self, text, padding=True):
        encrypted_key1 = self.des.encrypt(self.__keys[2], text, padding)
        decrypted_key2 = self.des.decrypt(self.__keys[1], encrypted_key1,
                                          False)
        return self.des.encrypt(self.__keys[0], decrypted_key2,
                                False)

    def decrypt(self, text, padding=True):
        decrypted_key1 = self.des.decrypt(self.__keys[0], text, False)
        encrypted_key2 = self.des.encrypt(self.__keys[1], decrypted_key1,
                                          False)
        return self.des.decrypt(self.__keys[2], encrypted_key2, padding)
