# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 20:22:56 2020

@author: etzellux
"""

from soru1modul import *

list1 = [1,2,7,3,5,2,10,27,13,12]

print(list1)

print("Toplam:",topla(list1))

print("Çarpım:",carp(list1))

print("Ortalama:",ortalama(list1))

print("En büyük eleman:",enBuyukEleman(list1))

print("En küçük eleman:",enKucukEleman(list1))

print("27'nin indexi:",ara(list1,27))

print("Listenin sıralanmış hali: ",sirala(list1))

print("Tekrar eden elemanlar çıkartılmış liste:",essiz(list1))


