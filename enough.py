from collections import defaultdict
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(delete_nth([1, 1, 1, 1], 2), [1, 1])
        
    def test_2(self):
        self.assertEqual(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
        
    def test_3(self):
        self.assertEqual(delete_nth([20,37,20,21], 1), [20,37,21])
        
        
def to_list(generator):
    def wrapper(*args):
        return list(generator(*args))
    return wrapper


@to_list
def delete_nth(collection, occurrences):
    counter = defaultdict(int)
    for item in collection:
        counter[item] += 1
        if counter[item] <= occurrences:
            yield item
        else:
            pass
        

if __name__ == "__main__":
    unittest.main()