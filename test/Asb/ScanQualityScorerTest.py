'''
Created on 02.05.2021

@author: michael
'''
import unittest
from Asb.ScanQualityScorer import AltoPageLayout


class ScanQualityScorererTest(unittest.TestCase):


    def testScoring(self):
        
        alto_page_layout = AltoPageLayout("Berlin_Example.jpg")
        self.assertEqual(0.47, round(alto_page_layout.scan_quality, 2))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()