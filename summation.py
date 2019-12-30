from functools import reduce
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(summation(5), 15)
        
    def test_2(self):
        self.assertEqual(summation(10), 55)


def summation(num: int) -> int:
    """
    returns the result of arithmetic summation of integers
    from 1 to given number
    """
    return reduce(lambda a,b: a+b, list(range(num+1)))


if __name__ == "__main__":
    unittest.main()
