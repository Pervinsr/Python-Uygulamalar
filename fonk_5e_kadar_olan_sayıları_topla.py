# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 19:05:13 2020

@author: pervi
"""

print()
print()
print()
print("FONKSİYONDALA TOPLAMA YAPMA 5'E KADAR OLAN SAYILARI TOPLA")  
def function(n,t):
    if n==1:
        return t
    else:
        t+=n
        print(n)
        return function(n-1,t)
        

n=5
toplam=0
toplam=function(n,toplam)
print("sonuc: ",toplam)