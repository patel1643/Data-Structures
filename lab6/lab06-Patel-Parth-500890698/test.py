import unittest
import random
from sorting import *


class test_mo3_quicksort(unittest.TestCase):
    def test_Empty_List(self):
        data = []
        mo3_quickSort(data)
        result = data
        self.assertEqual(result, [])

    def test_Unsorted_Integer_List(self):
        data = [1,2,3,3,32,4,5,3,5,43,4,3,45,3,45,434,4]
        resultTest = [1,2,3,3,32,4,5,3,5,43,4,3,45,3,45,434,4]
        quickSort(resultTest)
        mo3_quickSort(data)
        result = data
        self.assertEqual(result, resultTest)
    
    def test_Big_Unsorted_Integer_List(self):
        data = [random.randint(0,1000) for x in range(10000)]
        resultTest = data
        quickSort(resultTest)
        mo3_quickSort(data)
        result = data
        self.assertEqual(result, resultTest)


if __name__ == '__main__':
    unittest.main(argv=['first arg is ignored'], exit=False)
