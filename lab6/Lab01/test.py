import unittest
from mySolution import generate, calcScore
    
    
class test_genrate(unittest.TestCase):
    
        
    
        def test_generate_BaseCase(self):
            self.assertEqual(len(generate(0,0,list("abcdefghijklmnopqrstuvwxyz "))),0)
            
        def test_generate_programCase(self):
            self.assertEqual(len(generate(28,27,list("abcdefghijklmnopqrstuvwxyz "))),28)    
    
class test_calcScore(unittest.TestCase):
    
        def test_calcScore_complete(self):
            self.assertEqual(calcScore("methinks it is like a weasel","methinks it is like a weasel"),100.0)
    
        def test_calcScore_edgecase(self):
            self.assertEqual(calcScore("methcsjethwxltbpx rmwusjlheq","methinks it is like a weasel"),17.857142857142858)      
    
    
if (__name__ == "__main__"):
        unittest.main(argv=['first-arg-is-ignored'],exit=False)