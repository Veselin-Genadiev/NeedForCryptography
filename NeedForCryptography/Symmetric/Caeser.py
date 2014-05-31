from string import ascii_letters, ascii_uppercase


class Caeser:
    def __init__(self, key):
        self.__key = key % 26

    @staticmethod
    def shift(symbol, key):
        if not symbol.isalpha():
            return symbol

        letter_position = ascii_letters.index(symbol) % 26
        return ascii_uppercase[(letter_position + key) % 26]

    def encrypt(self, text):
        return ''.join(Caeser.shift(symbol, self.__key) for symbol in text)

    def decrypt(self, text):
        return ''.join(Caeser.shift(symbol, -self.__key) for symbol in text)
