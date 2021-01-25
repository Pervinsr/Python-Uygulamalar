# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 19:05:56 2020

@author: pervi
"""



def geometri(sekil):
   if len(sekil)==3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        if (a+b)>c and (a+c)>b and (b+c)>a:
            if(a==b) and (a==c) and(b==c):
                print("EŞKENAR ÜCGEN")
            elif(a==b) and (a==c):
                print("İkizkenar ücgen")
        else:
            print("ÜCGEN BELİRTMİYOR")
            
   elif len(sekil)==4:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        d=sekil[3]
        
        if(a==b)and (a==b) and(a==c)and(a==d):
            print("Kare")
        elif(a==c)and  (b==d):
            print("DİKDÖRTGEN")
        else:
            print("NORMAL DÖRTGEN")
            
   else:
         print("Herhangi bir şekil değildir.")
         
while (True):
     eleman_sayisi=int(input("eleman sayısı giriniz: " ))
     if(eleman_sayisi==3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri([a,b,c])
     elif(eleman_sayisi==4):
          a=int(input("a:"))
          b=int(input("b:"))
          c=int(input("c:"))
          d=int(input("c:"))
          geometri([a,b,c,d])
     else:
         print("LÜTFEN TEKRAR DENEYİNİZ")
         
         
         
         