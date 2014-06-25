from string import ascii_uppercase
from re import findall


class Feistel:
    '''
    Feistel is a block cipher. For input we need a number "n" and an array of
    dictionaries of tuple => tuple where tuple is of length n. tuples must
    contain numbers which will later be transformed to letters (based on the
    passed alphabet).
    '''

    def __init__(self, length, functions, alphabet=ascii_uppercase):
        self.__length = length
        self.__functions = functions
        self.__alphabet = alphabet

    def __XOR(self, left, right):
        return tuple(left[x] ^ right[x] for x in range(len(left)))

    def __hash(self, left, right, func):
        return right, self.__XOR(left, func[right])

    def encrypt(self, message, encryption=True):
        blocks = findall(r'.{{{}}}'.format(self.__length), message)
        blocks = list(map(tuple, [[self.__alphabet.index(char) for char
                                   in block] for block in blocks]))

        if(len(blocks) < 2):
            return message

        ciphertext = ''

        for pair in zip(blocks[::2], blocks[1::2]):
            left, right = pair
            functions = self.__functions

            if not encryption:
                functions = reversed(functions)

            for func in functions:
                if not encryption:
                    right, left = self.__hash(right, left, func)
                else:
                    left, right = self.__hash(left, right, func)

            mapped = map(lambda x: self.__alphabet[x], left + right)
            ciphertext += ''.join(mapped)

        return ciphertext + message[len(ciphertext):]

    def decrypt(self, message):
        return self.encrypt(message, False)
