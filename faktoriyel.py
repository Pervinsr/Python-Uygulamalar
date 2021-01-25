# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:12:13 2020

@author: pervi
"""

sayi = int(input("Sayi giriniz:"))

faktoriyel = 1

while(sayi>1):
    faktoriyel *= sayi
    sayi -= 1

print("Sonuc:",faktoriyel)






sayi = int(input("SAYI GİR:"))

faktoriyel = 1

for i in range(2,sayi+1):
    faktoriyel *= i

print("Sonuc:",faktoriyel)


