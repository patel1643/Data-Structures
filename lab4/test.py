import unittest
from mySolution import powerH, power, C


class test_genrate(unittest.TestCase):



    def test_powerH_NegativePower(self):
        self.assertEqual((power(405,-6,1)), 1)
    
    
    def test_powerH_allZeros(self):
        self.assertEqual((power(0,0,1)), 1)


    def test_power_NegativePower(self):
        self.assertEqual((powerH(5,-6)), 1)


    def test_power_decimal(self):
        self.assertEqual((powerH(2.5,5)), 97.65625)
    
    
    def test_C1(self):
        self.assertEqual(C(1,6), None)
   
    def test_C2(self):
        self.assertEqual(C(9,6), 84)    


if (__name__ == "__main__"):
    unittest.main(argv=['first-arg-is-ignored'],exit=False)