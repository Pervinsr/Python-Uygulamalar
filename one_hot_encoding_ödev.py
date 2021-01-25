# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:08:35 2020

@author: pervi
"""
#pandaları pd olarak içe aktar
#np'yi np olarak içe aktar
import pandas as pd
import numpy as np



A = np.linspace(2.0, 10.0, num=3)
B = ['köpek','kedi','kuş']
d = {'numarasi': A, 'categorical': B}
df = pd.DataFrame(d)
df['categorical'] = pd.Categorical(df['categorical'])
dfDummies = pd.get_dummies(df['categorical'], prefix = 'category')
df = pd.concat([df, dfDummies], axis=1)
print(df)









print()

print()


print()


print("<<<<<<<<<<<<<<<aaaa>>>>>>>>>>>>><<<<<")





import numpy as np

def one_hot_encode(x, n_classes):
    """
    One hot encode a list of sample labels. Return a one-hot encoded vector for each label.
    : x: List of sample Labels
    : return: Numpy array of one-hot encoded labels
     """
    return np.eye(n_classes)[x]

def main():
    list = [0,1,2,3,4,3,2,1,0]
    n_classes = 5
    one_hot_list = one_hot_encode(list, n_classes)
    print(one_hot_list)

if __name__ == "__main__":
    main()



print()
print()


print("<<<<<<<<<<<<<<<ÖDEVV>>>>>>>>>>>>><<<<<")

print()
print("ÖDEEVİM")
import numpy as np

def one_hot_encode1(x, n_classes):
    """
     örnek etiketlerin bir listesini kodlar. Her etiket için bir  kodlanmış vektör döndürün.
    : x: Örnek Etiketlerin Listesi
    : return: Numpy array of one-hot encoded labels
     """
    return np.eye(n_classes)[x]

def main():
    list = [0,1,2,3,0,3,1,2,0]
    n_classes = 5
    one_hot_list = one_hot_encode1(list, n_classes)
    print(one_hot_list)

if __name__ == "__main__":
    main()


print()
print()
print()



print()


print("<<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<")





import numpy as np
nb_classes = 6
data = [[2, 3, 4, 0]]

def indices_to_one_hot(data, nb_classes):
    """Convert an iterable of indices to one-hot encoded labels."""
    targets = np.array(data).reshape(-1)
    return np.eye(nb_classes)[targets]

indices_to_one_hot(data,nb_classes)
print(data)
print(nb_classes)




print()

print()

print()


print("<<<<<<<<<<<<<<<>>>>>>>>>>>>><<<<<")

print()





import pandas as pd
df = pd.DataFrame({
          'A':['a','b','a'],
          'B':['b','a','c']
        })



# Get one hot encoding of columns B
one_hot = pd.get_dummies(df['B'])
# Drop column B as it is now encoded
df = df.drop('B',axis = 1)
# Join the encoded df
df = df.join(one_hot)
print(df)  






