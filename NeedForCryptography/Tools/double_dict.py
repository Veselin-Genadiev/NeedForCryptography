class DoubleDict:
    def __init__(self, items=None):
        self.__reverse_dict = dict()
        self.__dict = dict()

        if(items is not None):
            for key, value in items:
                self.add(key, value)

    def get_key(self, value):
        return self.__reverse_dict[value]

    def get_value(self, key):
        return self.__dict[key]

    def add(self, key, value):
        self.__dict[key] = value
        self.__reverse_dict[value] = key
