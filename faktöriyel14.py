# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 03:06:01 2020

@author: pervi
"""

faktoriyel=1
 
while True:
     sayi=int(input("Negatif olmayan bir sayı girini."))
     if(sayi<= 0):
         print("negatif bir değer girdiniz.")
         
     else:
         for i in range(1,sayi+1):
             faktoriyel*=i
           
             
             
         print("faaaktoriyel:", faktoriyel)
         break
         