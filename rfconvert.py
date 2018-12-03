# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:56:00 2017

@author: P.Doulgeridis
"""

# RUN AS : python rfconvert.py RFPOLLASOSTO.txt RFPOLLASOSTOOUT.TXT 90573 8


import os
import sys
import time

file_in = sys.argv[1]
file_ot = sys.argv[2]
kodikosp = sys.argv[3]
controld = sys.argv[4]

def filetoliststrip(file):
    '''
  Function: filetoliststrip
  Description: Reads a file, stores in list (stripped)
  Input: File
  Output: List
  Usage: print (filetoliststrip("C:\\Users\\p.doulgeridis\\Desktop\\testpy.txt"))
  Notes: Path needs double \\ or reverse /
  '''
    file_in = str(file)
    lines = list(open(file_in, 'r'))
    content = [x.strip() for x in lines] 
    return content



def contoRF(inte, kod, psi):
    #print(inte)
    #print(type(inte))
    base=str(inte)
    #print (base)
    #print (type(base))
    if len(base) == 12:
        baseaug = str(kod) + str(psi) + "000" + base + "271500"
    else:
        baseaug = str(kod) + str(psi) + "00000" + base + "271500"
    #print (baseaug)
    #print (type(baseaug))
    baseaugn=int(baseaug)
    #print (baseaugn)
    #print (type(baseaugn))
    cd=baseaugn%97
    #print (cd)
    #print (type(cd))
    cdfixed= 98 - cd
    #print (cdfixed)
    if cdfixed < 10:
        cdfixed = "0" + str(cdfixed)
    else:
        cdfixed = str(cdfixed)
    
    if len(base) == 12:
        output = "RF" + str(cdfixed) + str(kod) + str(psi) + "000" + str(inte)
    else:
        output = "RF" + str(cdfixed) + str(kod) + str(psi) + "00000" + str(inte)
    
    # Validating its the correct calc
    #print ("Validating")
    temp2 = str(output[4:])
    #print (temp2)
    temp3 = temp2 + "2715" + str(cdfixed)
    #print (temp3)
    
    
    if int(temp3)%97 == 1:
        status = "ok"
    else:
        status = "notok"
        
    return (output, status)



#print (contoRF(123456789012, 90773, 8))
    
fileinlist = filetoliststrip(file_in)
out = open(file_ot, 'w')

for j in fileinlist:
    fixedj = str(j)
    calced=contoRF(fixedj, kodikosp, controld)
    out.write(str(fixedj) + "," + str(calced[0]) + "\n")
    
