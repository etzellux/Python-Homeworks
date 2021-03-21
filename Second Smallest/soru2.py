# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:19:58 2021

@author: etzellux
"""

liste = []


while True:
    print("Entry:",end="")
    text = input("")
    
    if text.lower() == "quit":
        break
    elif text.isalpha() and text != "quit":
        print("Geçersiz giriş")
        break
    else:
        liste.append(int(text))
    
print(liste)

for i in range(1,len(liste)): 
    key = liste[i]
    j = i - 1
    
    while j >= 0 and key < liste[j]:
        liste[j + 1] = liste[j]
        j -= 1
        
    liste[j + 1] = key
    
print(liste)

liste_uniq = []

for i in liste:
    if i not in liste_uniq:
        liste_uniq.append(i)

control = 0

for i in liste:
    if i == liste[0]:
        control += 1

if len(liste_uniq) > 1 and control == 1:
    
    second = liste_uniq[1]
    second_count = 0
    
    for i in range(0,len(liste)):
        if liste[i] == second:
            second_count += 1
            
    if second_count == len(liste):
        print([])
    elif second_count > 1:
        temp = []
        for i in range(0,second_count):
            temp.append(second)
        
        print(temp)
        
    else:
        print(second)
            
else:
    print([])
        

        

        