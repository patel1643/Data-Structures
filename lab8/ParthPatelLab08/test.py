import unittest
from mySolution import *



class test_genrate(unittest.TestCase):



    def test_1(self):
        x=['1', '*', '2', '+', '3', '*', '7']
        parsedList = parse(x)
        self.assertEqual(parsedList, ['+', ['*', ['1', [], []], ['2', [], []]], ['*', ['3', [], []], ['7', [], []]]])    

    def test_2(self):
        x=[['5'], '-', ['4'], '+', '6','+',[['3', '+', '1'], '!']]
        parsedList = parse(x)
        self.assertEqual(parsedList, ['+', ['+', ['-', ['5', [], []], ['4', [], []]], ['6', [], []]], ['!', ['+', ['3', [], []], ['1', [], []]], []]])    
        

    def test_3(self):
        x=[['5', '+', '2'],'+',[['3', '+', '1'], '!']]
        parsedList = parse(x)
        self.assertEqual(parsedList, ['+', ['+', ['5', [], []], ['2', [], []]], ['!', ['+', ['3', [], []], ['1', [], []]], []]])           
    
    def test_4(self):
        x= [['4', '+', '3'], '*', '7', '+', [['8' , '+', '4'], '!']]
        parsedList = parse(x)
        self.assertEqual(parsedList, ['+', ['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]], ['!', ['+', ['8', [], []], ['4', [], []]], []]])

    def test_5(self):
        x=['4','/',['8', '!'],'-',['9', '+', '2'], '!']
        parsedList = parse(x)
        self.assertEqual(parsedList, ['-', ['/', ['4', [], []], ['!', ['8', [], []], []]], ['!', ['+', ['9', [], []], ['2', [], []]], []]])        

    def test_6(self):
        x=['4', '+', [['3', '+', '1'], '!']]	
        parsedList = parse(x)
        self.assertEqual(parsedList, ['+', ['4', [], []], ['!', ['+', ['3', [], []], ['1', [], []]], []]])     
    
    def test_7(self):
        x=['2', '/', [['9', '-', '7'], '!']]	
        parsedList = parse(x)
        self.assertEqual(parsedList, ['/', ['2', [], []], ['!', ['-', ['9', [], []], ['7', [], []]], []]])              

if (__name__ == "__main__"):
    unittest.main(argv=['first-arg-is-ignored'],exit=False)