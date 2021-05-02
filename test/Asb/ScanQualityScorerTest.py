'''
Created on 02.05.2021

@author: michael
'''
import unittest
from Asb.ScanQualityScorer import AltoPageLayout
from Asb.Extractor import process


class ScanQualityScorererTest(unittest.TestCase):


    def testScoring(self):
        
        alto_page_layout = AltoPageLayout("Berlin_Example.jpg")
        self.assertEqual(0.47, round(alto_page_layout.scan_quality, 2))
        
    def test_textract(self):
        
        text, score = process("Berlin_Example.jpg")
        
        self.assertEqual(328, len(text))
        self.assertEqual(0.47, round(score, 2))

    def test_textract_no_image(self):
        
        text, score = process("test.txt")
        
        self.assertEqual(b"Test", text)
        self.assertEqual(None, score)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()