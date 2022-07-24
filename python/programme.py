from math import *

lexique=["le", "la", "les" ,"un" ,"une" ,"un" ,"deux" ,"trois" ,"quatre" ,
"cinq" ,"six" ,"sept" ,"huit" ,"neuf" ,"dix" ,"onze" ,"douze" ,"treize" ,
"quatorze" ,"quinze"]

def hamming(str1,str2):
    a=abs(len(str1)-len(str2))
    if len(str1)<=len(str2):
        min=len(str1)
    else:
        min=len(str2)
    for k in range(min):
        if str1[k]!=str2[k]:
            a+=1
    return a



