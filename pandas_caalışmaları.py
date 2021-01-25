# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:46:06 2020

@author: pervi
"""

import pandas as pd #burada pandası çağırıp pd kısaltması ile kullanacağımızı belirtiyoruz
data = [1,7,3,7,9,10]
seri = pd.Series(data) #burada elemanları yazıp seriyi tanımlıyoruz
seri #seriyi yazdırıyoruz




index = ["İstanbul", "Ankara", "İzmir", "Yalova", "Adana", "Diyarbakır"] #Doğru
index2 = ["İstanbul", "Ankara", "İzmir", "Yalova", "Adana", "Diyarbakır", "Bursa"] #Yalnış
pd.Series(data = data , index = index)









