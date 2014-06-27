from math import ceil
from crypto.tools.doubledict import DoubleDict
from re import findall
from collections import OrderedDict
from itertools import count


class Playfair:
    '''
    To use the cipher simply pass a key which is a plaintext. Please make sure
    that the key is of length which is a square of some number and has only
    unique characters. Otherwise the cipher will be much less secure.
    '''
    def __init__(self, key):
        self.__key = self.matrix_map(''.join(list(OrderedDict.fromkeys(key))))

    def matrix_map(self, key):
        rows = int(ceil(len(key) ** 0.5))
        letter_map = [(letter, (index // rows, index % rows)) for
                      index, letter in enumerate(key)]
        return DoubleDict(letter_map)

    def encrypt(self, text, offset=1):
        text = ''.join([letter for letter in text
                        if self.__key.has_key(letter)])

        if len(text) % 2 == 1:
            raise ValueError("Text must be of even length!")

        return ' '.join(self.__encrypt_pair(pair, offset)
                        for pair in findall(r'..', text))

    def decrypt(self, text, offset=-1):
        return self.encrypt(text, offset)

    def __encrypt_pair(self, pair, offset=1):
        first, second = pair

        if(first == second):
            return pair

        first_row, first_col = self.__key.get_value(first)
        second_row, second_col = self.__key.get_value(second)

        if(first_col == second_col):
            return self.__cyclic_vertical(pair, offset)
        elif(first_row == second_row):
            return self.__cyclic_horizontal(pair, offset)
        else:
            return self.__switched_columns(pair)

    def __decrypt_pair(self, pair):
        return self.__encrypt_pair(pair, -1)

    def __cyclic_shift_row(self, row, col, offset):
        if self.__key.has_value((row + offset, col)):
            return (row + offset, col)
        elif row == 0 and offset < 0:
            for index in count():
                if not self.__key.has_value((index, col)):
                    return (index - 1, col)
        else:
            return (0, col)

    def __cyclic_shift_col(self, row, col, offset):
        if self.__key.has_value((row, col + offset)):
            return (row, col + offset)
        elif col == 0 and offset < 0:
            for index in count():
                if not self.__key.has_value((row, index)):
                    return (row, index - 1)
        else:
            return (row, 0)

    def __cyclic_vertical(self, pair, offset):
        first, second = pair
        first_row, first_col = self.__key.get_value(first)
        first_coordinates = \
            self.__cyclic_shift_row(first_row, first_col, offset)
        second_row, second_col = self.__key.get_value(second)
        second_coordinates = \
            self.__cyclic_shift_row(second_row, second_col, offset)

        return self.__key.get_key(first_coordinates) + \
            self.__key.get_key(second_coordinates)

    def __cyclic_horizontal(self, pair, offset):
        first, second = pair
        first_row, first_col = self.__key.get_value(first)
        first_coordinates = \
            self.__cyclic_shift_col(first_row, first_col, offset)
        second_row, second_col = self.__key.get_value(second)
        second_coordinates = \
            self.__cyclic_shift_col(second_row, second_col, offset)

        return self.__key.get_key(first_coordinates) + \
            self.__key.get_key(second_coordinates)

    def __switched_columns(self, pair):
        first, second = pair
        first_row, first_col = self.__key.get_value(first)
        second_row, second_col = self.__key.get_value(second)
        first_col, second_col = second_col, first_col

        return self.__key.get_key((first_row, first_col)) + \
            self.__key.get_key((second_row, second_col))
