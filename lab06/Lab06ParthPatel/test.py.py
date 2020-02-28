import unittest
import random
from mySolution import mo3_quickSort, quickSort


class test_mo3_quicksort(unittest.TestCase):
    def test_01(self):
        list1 = []
        mo3_quickSort(list1)
        result = list1
        self.assertEqual(result, [],"Tested Empty List")

    def test_02(self):
        list1 = [3,4,22,50,55,31,43,65,76,34,56,78,10,29,48,76]
        list2 = [3,4,22,50,55,31,43,65,76,34,56,78,10,29,48,76]
        quickSort(list2)
        mo3_quickSort(list1)
        result = list1
        self.assertEqual(result, list2,"Tested Sample Unsorted List")


if __name__ == '__main__':
    unittest.main(argv=['first arg is ignored'], exit=False)