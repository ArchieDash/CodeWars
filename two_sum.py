import unittest
from itertools import combinations


def two_sum(numbers: list, target: int) -> list:
    for combination in combinations(numbers, 2):
        if sum(combination) == target:
            return [index for index, element in enumerate(numbers) if element in combination]
        

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(two_sum([1, 2, 3], 4), [0, 2])
        
    def test_2(self):
        self.assertEqual(two_sum([1234, 5678, 9012], 14690), [1, 2])
        
    def test_3(self):
        self.assertEqual(two_sum([2, 2, 3], 4), [0,1])
        

unittest.main()