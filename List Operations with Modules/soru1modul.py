# -*- coding: utf-8 -*-

def topla(liste):
    toplam = 0
    for i in liste:
        toplam += i
    return toplam

def carp(liste):
    carpim = 1
    for i in liste:
        carpim *= i
    return carpim

def ortalama(liste):
    toplam = topla(liste)
    return toplam / len(liste)

def enBuyukEleman(liste):
    buyuk = liste[0]
    for i in liste:
        if i > buyuk:
            buyuk = i
    return buyuk

def enKucukEleman(liste):
    kucuk = liste[0]
    for i in liste:
        if i < kucuk:
            kucuk = i
    return kucuk

def ara(liste,aranan):
    index = 0
    for i in liste:
        if i == aranan:
            return index
    print("İstenen eleman bulunamadı")
    
def sirala(liste):
    for i in range(1,len(liste),1):
        key = liste[i]
        j = i-1
        while j >= 0 and liste[j] > key:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = key
    return liste
        
def essiz(liste):
    list1 = sirala(liste)
    for i in range(0,len(list1)-2,1):
        if list1[i] == list1[i+1]:
            del list1[i+1]
    return list1
        

    