from math import ceil
from Tools.double_dict import DoubleDict
from re import findall


class Playfair:
    def __init__(self, key):
        self.__key = self.matrix_map(''.join(list(set(key))))

    def matrix_map(self, key):
        rows = ceil(len(key) ** 0.5)
        letter_map = [(letter, (index / rows, index % rows)) for
                      index, letter in enumerate(key)]
        return DoubleDict(letter_map)

    def encrypt(self, text, offset=1):
        text = ''.join([letter for letter in text
                        if self.__key.has_key(letter)])

        if len(text) % 2 == 1:
            raise AttributeError("Text's symbols included in the key must be of even count!")

        return ' '.join(self.__encrypt_pair(pair, offset) for pair
                        in findall(r'..', text))

    def decrypt(self, text, offset=-1):
        return self.encrypt(self, text, offset)

    def __encrypt_pair(self, pair, offset=1):
        first, second = pair

        if(first == second):
            return (first, second)

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
        if not self.__key.has_value((row + offset, col)):
            return (row + offset, col)
        else:
            return (0, col)

    def __cyclic_shif_col(self, row, col, offset):
        if not self.__key.has_value((row, col + offset)):
            return (row, col + offset)
        else:
            return (row, 0)

    def __cyclic_vertical(self, pair, offset):
        first, second = pair
        first_row, first_col = \
            self.__cyclic_shift(self.__key.get_value(first), offset)
        second_row, second_col = \
            self.__cyclic_shift(self.__key.get_value(second), offset)

        return (self.__key.get_key((first_row, first_col)),
                self.__key.get_key((second_row, second_col)))

    def __cyclic_horizontal(self, pair, offset):
        first, second = pair
        first_row, first_col = \
            self.__cyclic_shif_col(self.__key.get_value(first), offset)
        second_row, second_col = \
            self.__cyclic_shif_col(self.__key.get_value(second), offset)

        return (self.__key.get_key((first_row, first_col)),
                self.__key.get_key((second_row, second_row)))

    def __switched_columns(self, pair):
        first, second = pair
        first_row, first_col = self.__key.get_value(first)
        second_row, second_col = self.__key.get_value(second)
        first_col, second_col = second_col, first_col

        return (self.__key.get_key((first_row, first_col)),
                self.__key.get_key((second_row, second_col)))
