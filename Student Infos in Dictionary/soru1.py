# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:01:00 2020

@author: etzellux
"""
ogrenci_listesi = {"2312323":"Mehmet"}

while True:
    control = input("Sözlüğe yeni kayıt eklemek istiyor musunuz? [E/H]:")
    control = control[0]
    
    if control == "H" or control == "h":
        break
    
    key_ = input("Öğrenci numaranızı yazınız:")
    value_ = input("Adınızı yazınız:")
    ogrenci_listesi[key_] = value_
    
for i,j in ogrenci_listesi.items():
    print(i," ",j)
    
    