from math import ceil
from Tools.double_dict import DoubleDict


class Playfair:
    def __init__(self, key):
        self.__key = self.matrix_map(key)

    def matrix_map(self, key):
        rows = ceil(len(key) ** 0.5)
        letter_map = [(letter, (rows / index, rows % index)) for
                      index, letter in enumerate(key)]
        return DoubleDict(letter_map)
