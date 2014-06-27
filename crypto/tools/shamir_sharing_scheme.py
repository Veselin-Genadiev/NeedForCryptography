from random import SystemRandom


class ShamirSharingScheme:
    '''
    Shamir sharing scheme is used to share a secret in a party of count 'n'
    and evenry party of 'k' or more users can recover the secret.
    '''
    def __init__(self, secret, parts, subset_parts):
        if subset_parts >= parts:
            raise ValueError('Subset parts must be less or equal'
                             'than all parts count')

        rand = SystemRandom()
        parameters = rand.sample(range(1, secret),
                                 subset_parts - 1)

        polynom = lambda x: secret + sum(c * (x ** (i + 1)) for i, c
                                         in enumerate(parameters))

        self.__subset_parts = subset_parts
        self.__points = [(x, polynom(x)) for x in range(1, parts + 1)]

    @property
    def points(self):
        return self.__points

    def reconstruct(self, points):
        if ((set(points) & set(self.__points) != set(points)
             or len(set(points)) < self.__subset_parts)):
            raise ValueError('Wrong or not enough points')

        points = points[:self.__subset_parts]
        parts = [1] * self.__subset_parts

        for i in range(0, self.__subset_parts):
            parts[i] *= points[i][1]

            for j in range(0, self.__subset_parts):
                if i != j:
                    parts[j] *= -points[i][0] / (points[j][0] - points[i][0])

        return round(sum(parts))
