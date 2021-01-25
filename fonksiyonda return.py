# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:19:55 2020

@author: pervi
"""
"""
def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):  
        faktoriyel*=i    #burada faktöriyeli hesaplattım.
   #▀ print("faktöriyeel",faktoriyel)   #burada ekrana yazılmasını sağladık.
    
    return faktoriyel  #dış dünyaya birşey gönderme /döndürme işlemi

    
        
sayi=int(input("sayı giriniz: "))

a=factoriel(sayi)  # bir değere eşitlemem lazım 
print(a)   # a yı yazdırdım


"""
 #BAŞKA BİR FONKSİYON 
 
def kokbul(a,b,c):
    delta =(b*b - 4*a*c)
    if(delta<0):
       #  print("REEL KÖK BULUNAMADI")  #bunu böyle yazınca none yazıyordu
       k="reel kök bulunamadı"
      
       return(k)
     
    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/(2*a)
        
    return(x1,x2)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kokbul(a,b,c)

print(sonuc)




