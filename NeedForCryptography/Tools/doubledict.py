class DoubleDict:
    def __init__(self, items=None):
        self.__reverse_dict = dict()
        self.__dict = dict()

        if(items is not None):
            for key, value in items:
                self[key] = value

    @property
    def keys(self):
        return self.__dict.keys

    @property
    def values(self):
        return self.__reverse_dict.keys

    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def get_key(self, value):
        return self.__reverse_dict[value]

    def get_value(self, key):
        return self.__dict[key]

    def add(self, key, value):
        self.__dict[key] = value
        self.__reverse_dict[value] = key

    def has_key(self, key):
        return key in self.__dict

    def has_value(self, value):
        return value in self.__reverse_dict
