from tools.shamir_sharing_scheme import ShamirSharingScheme
from itertools import combinations
import unittest


class ShamirSharingSchemeTests(unittest.TestCase):
    def test_reconstruct(self):
        for secret in range(50, 80):
            sh = ShamirSharingScheme(secret, 10, 5)
            for combination in combinations(sh.points, 5):
                self.assertEqual(secret, sh.reconstruct(list(combination)))

    def test_wrong_subset_part_length(self):
        sh = ShamirSharingScheme(2048, 10, 5)
        self.assertRaises(ValueError, sh.reconstruct, sh.points[:4])
        self.assertRaises(ValueError, ShamirSharingScheme, 200, 10, 11)
