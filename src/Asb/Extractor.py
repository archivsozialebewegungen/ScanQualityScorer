'''
Created on 02.05.2021

@author: michael
'''

import textract
from Asb.ScanQualityScorer import AltoPageLayout

def process(filename):
        
    text = textract.process(filename)
    try:
        alto_layout = AltoPageLayout(filename)
        score = alto_layout.scan_quality
    except:
        score = None
            
    return text, score