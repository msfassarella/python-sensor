#!/usr/bin/python
#coding: utf-8

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

filepath = "data/"
filename = "20190704-sensortile_log_n000.csv"


try:
    df = pd.read_csv(filepath + filename,",", header=0)
    #imprime as primeiras 5 linhas do arquivo
    print(df.head(5))
    #imprime as ultimas 5 linhas do arquivo
    print(df.tail(5))
except:
    print("Arquivo não encontrado")
    raise

plt.scatter(df['T [ms]'], df['AccX [mg]'],edgecolors='#ff0000')
plt.scatter(df['T [ms]'], df['AccY [mg]'],edgecolors='#00ff00')
plt.scatter(df['T [ms]'], df['AccZ [mg]'],edgecolors='#0000ff')

maximo = df.max(['AccX'])
print(maximo)
x1,x2,y1,y2 = plt.axis()
#print("x1 = " + x1 + "x2 = " + x2 + "y1 = " + y1 + "y2 = " + y2)



#plt.show()


