# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:38:37 2019

@author: Arjan
"""

class spaceReplace:
    def __init__(self, string):
        self.string = string
        
    def replace(self):
        newString = "" 
        for i in self.string:
            if i == " ":
                i = "%20"
            newString = newString + i
        return newString
    
overwrite = spaceReplace("My name is Arjan")
print(overwrite.replace())
