from string import ascii_uppercase
from collections import OrderedDict
from numpy.linalg import inv, det
from numpy import dot


class Hill:
    '''
    Hill cipher. For encrypt/decrypt we need an invertible square matrix of
    elements with length of [0, 25] and a rank eqaul to the length of the text
    which will be encrypted. The algorithm is ment to be used for encrypting
    a single word only. By default English uppercase alphabet is used.
    '''
    def __init__(self, matrix, alphabet=ascii_uppercase):
        if det(matrix) == 0:
            raise ValueError('Determinant must be invertible')

        self.__alphabet = ''.join(list(OrderedDict.fromkeys(alphabet)))
        self.__modulo = len(self.__alphabet)
        self.__matrix = [list(map(lambda col: col % self.__modulo, row))
                         for row in matrix]

    def encrypt(self, text, encryption=True):
        vector = self.__vectorize(text)
        matrix = self.__matrix

        if not encryption:
            matrix = (inv(self.__matrix) * det(matrix)).tolist()
            matrix = [list(map(lambda col: int(col) % 26, row))
                      for row in matrix]

        encrypted_vector = dot(matrix, vector).tolist()
        encrypted_vector = [x % self.__modulo for x in encrypted_vector]

        encrypted_text = self.__textify(encrypted_vector)
        return encrypted_text

    def decrypt(self, text):
        return self.encrypt(text, False)

    def __vectorize(self, text):
        return [self.__alphabet.index(symbol) for symbol in text]

    def __textify(self, vector):
        return ''.join(self.__alphabet[i] for i in vector)
