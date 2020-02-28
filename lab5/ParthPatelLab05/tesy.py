import unittest
from mySolution import HashTable


class test_genrate(unittest.TestCase):
    H = HashTable()
    H.put(54,"cat")
    H.put(26,"dog")
    H.put(22,"c at")
    H.put(34,"ca t")
    H.put(46,"dog ")
    H.put(52,"c a t")
    H.put(64,"ca  t")
    H.put(86,"d o g  ")
    H.put(62,"c a t  ")
    H.put(14,"ca 2t")
    H.put(116,"d o1g  ")
    H.put(117,"do1g  ")   
    H.put(44,"goat")
    H.put(55,"pig")
    H.put(20,"chicken")
    H.put(42,"goat")
    H.put(51,"pig")
    H.put(24,"chicken")
    
    
    def test_1(self):
        self.assertEqual(self.H.get(0), None)
   
    def test_2(self):
        self.assertEqual(self.H.get(46), 'dog ')
    
    def test_3(self):
        self.assertEqual(self.H.get(117), 'do1g  ')
        
    def test_4(self):
        self.assertEqual(self.H.get(-46), None)
        
    def test_5(self):
        self.assertEqual(self.H.get(44), 'goat')    
        
    def test_6(self):
        self.assertEqual(self.H.get(20), 'chicken')

    def test_7(self):
        self.assertEqual(self.H.get(51), 'pig')

    def test_8(self):
        self.assertEqual(self.H.get(22), 'c at')
    
    
if (__name__ == "__main__"):
    unittest.main(argv=['first-arg-is-ignored'],exit=False)
    
    

