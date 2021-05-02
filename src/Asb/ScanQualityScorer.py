'''
Created on 02.05.2021

@author: michael
'''
from xml.dom.minidom import Element, parseString
import pytesseract
import sys
from PIL import Image
import textract

class StringObject:
    '''
    Helper class for string representations in the AltoPageLayout class.
    '''
    def __init__(self, stringElement: Element):
        
        self.element = stringElement
    
    def _get_confidence(self):
        
        return float(self.element.getAttribute("WC"))
    
    def _get_string_length(self):
        
        return len(self.get_text())

    def get_text(self):
        
        return self.element.getAttribute("CONTENT")
    
    len = property(_get_string_length)
    confidence = property(_get_confidence)


class AltoPageLayout:
    '''
    This is a class to get information about an image using OCR.
    '''
    
    def __init__(self, file_name, language: str='deu'):

        img = Image.open(file_name)
        self.dom = parseString(pytesseract.image_to_alto_xml(img,lang=language).decode('utf-8'))
    
    def _get_confidence(self):
        
        characters = 0
        conf = 0.0
        for string in self.get_all_strings():
            characters += string.len
            conf += string.confidence * string.len
        return conf / characters
            
    def get_all_strings(self) -> [StringObject]:

        strings = []
        for string in self.dom.getElementsByTagName("String"):
            strings.append(StringObject(string))
        return strings

    scan_quality = property(_get_confidence)

if __name__ == '__main__':
    
    input_file = sys.argv[1]
    alto_page_layout = AltoPageLayout(input_file)
    print("Scan quality for %s is %f." % (input_file, alto_page_layout.scan_quality))