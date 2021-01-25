# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:18:08 2020

@author: pervi
"""

import pandas as pd

veriseti=pd.read_excel("./data2/chronic_kidney_disease.xls")
nitelikler=veriseti.columns  #başlıklarım yani sütunlarım
print(nitelikler)

print()
print()
print("burda ilk satırı yazdırdım...")
datalar=veriseti.values
for data in datalar:  # ilk satırdaki elemanları 
    print(data)
    break

print()
print("Data sayisi:",len(datalar)) #bunlar benim datalarım  elemanlarım satırlarım



print()
print("Kaç tane nitelik sayisi var:",len(nitelikler)-1)  #sütun sayım




print()
birinciNitelik=datalar[:,0]   #burda ilk sütundaki verileri getirdim
print("1 sütündaki:",birinciNitelik)



print()
print()
print("x ve y dekileri gördüm burda")
print()

x=datalar[:,0:24]   #158 tane elemanım 24 tane sürun coloumns
y=datalar[:,24]

print("X veri uzayı:",x.shape)  #hepsini al
print("y verileri:",len(y))





print()
print()

print("ATT sayısı:",len(nitelikler))

print()
print()
print("kaç niteliğim var ")

x=datalar[:,0:len(nitelikler)-3]
print(x.shape)




print()
print("Targetlar hangi sütunda")

y=datalar[:,len(nitelikler)-3]
y2=datalar[:,len(nitelikler)-2]
y3=datalar[:,len(nitelikler)-1]
print("y:",len(nitelikler)-3,"y2:",len(nitelikler)-2,"y3:",len(nitelikler)-1)
print()
print()





print("   <<<<Hasta olanlara olmayanlara bakalım 1 ve 0>>>>  ")
print()


def hastaBilgisi(y):
    print(y)  #o sütundaki elemanlarım
    print()
    hs,hos=0,0
    for veri in y: 
        if veri==0.0:
             hos+=1
        else:
             hs+=1
    print("Hasta sayisi:",hs)    
    print("Hasta olmayan sayisi: ",hos)    
        

hastaBilgisi(y)
print()

print("  <<<<<<<<Yaşların ortalamasını bulalım.>>>>>>>>>>>")
print()


def yas_ortalaması(yasListem):
    t=0  #toplamları başlangıcta 0
    for yaslar in yasListem:  #yaslara aktar
        t+=yaslar  #yasların her birni topla
    ortalama=t/len(yasListem)  #yasları listenin eleman sayısına böl
    print(ortalama)
    return round(ortalama,2)  #virgülden son 2 basamak alalım


yaslarVerisi=datalar[:,0]
print("Yas ortalaması:",yas_ortalaması(yaslarVerisi))



print()
print()
print("LİSTEMİ YAZIDR")

def evet_sayisi(listem):
    evet_hayir = []

    for a in range (0, len(y)):
       if(int(y[a])==1):  #float int yaptım
           evet_hayir.append('evet')  #indexine atama 
       else:
           evet_hayir.append('hayir')
    print(evet_hayir)    
   
listem=datalar[:,len(nitelikler)-3] 
evet_sayisi(listem)

















"""

a = ("banana", "grape", "cherry")
b = list(a)
b[0] = "apple"
a = tuple(b)

print(a)  # ("apple", "grape", "cherry")








"""







"""
def guncelle(listem):
    veriseti.execute("SELECT * FROM listem")
    
    datalar=listem.fetchall()
    print("ilk değerler...")
    for i in datalar:
        print(i)

    listem=datalar("UPDATE listem SET degerler=1 WHERE degerler='EVET' ")
    
    listem=datalar("SELECT * FROM listem")

listem=datalar[:,len(nitelikler)-3] #bu ilk targetden alıcak -3 yanı
guncelle(listem)

"""










