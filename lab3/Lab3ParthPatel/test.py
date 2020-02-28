import unittest
from mySolution import Stack, infixToPostfixEval, doMath, factorial


class test_genrate(unittest.TestCase):



    def test_inFixtoPostfixEval1(self):
        self.assertEqual(infixToPostfixEval('( 2 + 2 ) ! + 4 - 2 + 8'), ('2 2 + ! 4 + 2 - 8 +', 34))
    
    
    def test_inFixtoPostfixEval2(self):
        self.assertEqual(infixToPostfixEval('( 2 ! 2 ) ! ! 4 ! 2 ! 8'), ('2 2 ! ! 4 ! 2 ! 8 !', 40320))


    def test_inFixtoPostfixEval3(self):
        self.assertEqual(infixToPostfixEval('( 2 + 2 )  + 4 + 2 + 8'), ('2 2 + 4 + 2 + 8 +', 18))


    def test_inFixtoPostfixEval4(self):
        self.assertEqual(infixToPostfixEval('( 2 - 2 ) ! - 4 - 2 - 8'), ('2 2 - ! 4 - 2 - 8 -', -13))


    def test_inFixtoPostfixEval5(self):
        self.assertEqual(infixToPostfixEval('( 2 / 2 ) * 4 * 2 * 8'), ('2 2 / 4 * 2 * 8 *', 64.0))
    


if (__name__ == "__main__"):
    unittest.main(argv=['first-arg-is-ignored'],exit=False)