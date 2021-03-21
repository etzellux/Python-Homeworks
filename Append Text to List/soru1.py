# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:45:26 2021

@author: etzellux
"""

liste = []

while True:
    text = input("")
    
    if text.lower() == "quit":
        break
    else:
        liste.append(text)
        
for i in range(1,len(liste) + 1):
    print(liste[-i])