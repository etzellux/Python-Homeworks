# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:25:19 2020

@author: etzellux
"""

def code(message,mod,rate):
    
    newMessage = ""
    alphUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphLow = "abcdefghijklmnopqrstuvwxyz"
    
    check_ = len(alphUp)-1
    
    alph = alphUp + alphLow
    
    if mod == 0:
        rate *= 1
    else:
        rate *= -1
    
    for i in message:
        
        index_ = alph.index(i)
        
        if index_ <= check_ and index_ > check_-3 and rate > 0:
            index_ -= check_ +1
            rate *= -1
            
        elif index_ >= 0 and index_ < 3 and rate < 0:
            index_ += check_ +1
            
        elif index_ <= check_*2 and index_ > check_*2 -3 and rate > 0:
            index_ -= check_ +1
            rate *= -1
            
        elif index_ >= check_ and index_ < check_ +3 and rate < 0:
            index_ += check_ +1
            
        index_ += rate
            
        newMessage += alph[index_]
        
    return newMessage
            
        
check_ = "E"
while True:
    
    if check_ == "E" or check_ == "e":
        
        control_ = input("Yazmak için Y Çözmek için C ye basınız:")
        
        if control_ == "Y" or control_ == "y":
            mod = 0
            
        elif control_ == "C" or control_ == "c":
            mod = 1
            
        rate = int(input("Anahtar sayı giriniz:"))
        message = input("Mesaj giriniz:")
        
        newMessage = code(message,mod,rate)
        print("Yeni mesaj: ",newMessage)
            
    elif check_ == "H" or check_ == "h":
        break
    else:
        continue
    
    check_ = input("Devam etmek istiyor musunuz [E/H]:")
       
    