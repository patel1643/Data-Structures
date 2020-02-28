import unittest
from mySolution import *



class test_genrate(unittest.TestCase):
    
        
    
        def test_1(self):
                tree = BinaryTree("+")
                env = [["i", 20], ["j", 30]]
                insertLeft(tree, "i")
                insertRight(tree, "j")
                result = evalTree(tree, env)
                self.assertEqual(result, '50',"50 Expected")    
   
        def test_2(self):
                tree = BinaryTree("+")
                env = [["a", 10], ["b", -30]]
                insertLeft(tree, "a")
                insertRight(tree, "b")
                result = evalTree(tree, env)
                self.assertEqual(result, '-20',"-20 Expected")
    
        def test_3(self):
                tree = BinaryTree("/")
                env = [["c", 7], ["d", -14]]
                insertLeft(tree, "c")
                insertRight(tree, "d")
                result = evalTree(tree, env)
                self.assertEqual(result, '-0.5',"-0.5 Expected")
            
        def test_4(self):
                tree = BinaryTree("-")
                env = [["e", 7], ["f", 4]]
                insertLeft(tree, "e")
                insertRight(tree, "f")
                result = evalTree(tree, env) 
                self.assertEqual(result, '3',"3 Expected")
            
        def test_5(self):
                tree = BinaryTree("*")
                env = [["g", 27], ["h", 4]]
                insertLeft(tree, "g")
                insertRight(tree, "h")
                result = evalTree(tree, env)
                self.assertEqual(result, '108',"108 Expected")
        
    
if (__name__ == "__main__"):
        unittest.main(argv=['first-arg-is-ignored'],exit=False)