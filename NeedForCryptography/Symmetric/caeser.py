from string import ascii_uppercase
from collections import OrderedDict


class Caeser:
    '''
    Caeser cipher is based on shifting a symbol with "key" positions on the
    right. Users can choose a custom alphabet too.
    '''
    def __init__(self, key, alphabet=ascii_uppercase):
        self.__alphabet = list(OrderedDict.fromkeys(alphabet))
        self.__modulo = len(self.__alphabet)
        self.__key = key % self.__modulo

    def __shift(self, symbol, key):
        if symbol not in self.__alphabet:
            return symbol

        letter_position = self.__alphabet.index(symbol) % self.__modulo
        return self.__alphabet[(letter_position + key) % self.__modulo]

    def encrypt(self, text):
        return ''.join(self.__shift(symbol, self.__key) for symbol in text)

    def decrypt(self, text):
        return ''.join(self.__shift(symbol, -self.__key) for symbol in text)
