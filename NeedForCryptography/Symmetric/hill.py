import Tools.utilities as utilities


class Hill:
    '''
    Hill cipher. For encrypt/decrypt we need an invertible square matrix of
    indexes with length of [0, 25] and a rank eqaul to the length of the text
    which will be encrypted. The algorithm is ment to be used for encrypting
    a single word only.
    '''
    def __init__(self, matrix):
        if utilities.det(matrix) == 0:
            raise ValueError('Determinant must be invertible')

        self.__matrix = matrix

    def encrypt(text):
        text = text.upper()
        return text
