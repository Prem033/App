# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:45:56 2019

@author: prem.kumar.rayappan
"""
from fuzzywuzzy import fuzz
cc =0;
max=0;
def getdatavalue(a,b,ST):
    length = len(a)
    if length>0:
        for i in range(length):
                global max
                l=fuzz.token_set_ratio((a[i].text),ST)
                if max<l:
                    global cc
                    max=l
                    cc=i
                   
                    
        return (a[cc].text, b[cc].text) 
    else:
        return ("Product Not found","Associated Prize Not found")