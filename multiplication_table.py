import numpy as np
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(multiplication_table(2,2), [[1,2],[2,4]])
    
    def test_2(self):
        self.assertEqual(multiplication_table(3,3), [[1,2,3],[2,4,6],[3,6,9]])
        

def multiplication_table(a: int, b: int) -> list:
    a = np.arange(1, a + 1)
    b = np.arange(1, b + 1).reshape(b, 1)
    return (a * b).T.tolist()


if __name__ == "__main__":
    unittest.main()