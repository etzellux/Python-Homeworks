# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:54:02 2020

@author: etzellux
"""

def sorgula(formul):
    sayac1 = 0
    sayac2 = 0
    for i in formul:
        if i == "(":
            sayac1 += 1
        elif i == ")":
            sayac2 += 1
    
    if sayac1 == sayac2:
        print("Hata yok")
    else:
        if sayac1 > sayac2:
            print(sayac1-sayac2," adet","(","fazla")
        else:
            print(sayac2-sayac1," adet",")","fazla")
            
        
formul = "((9*7)/((27+7)"
print(formul)
sorgula(formul)
   