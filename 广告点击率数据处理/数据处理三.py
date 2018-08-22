# coding:utf-8

import  pandas as pd
import numpy as np
with open(r'E:\蒋子龙给吴再培\kaggle-2014-criteo\PaxHeader\test.txt') as f:
    data = pd.read_table(f,nrows=5,index_col=None,header=None)

data = data.fillna(2)
x = data.iloc[:,15::]

# print(x)

n,m = x.shape
for i in range(n):
    for j in range(m):
        x.iloc[i,j] = int(str(x.iloc[i,j]),16)
x = x.fillna(1)
# print(x.isnull().sum())
# print((x.iloc[0,0]-np.mean(x.iloc[:,0]))/np.std(x.iloc[:,0]))
def Standardize(data):
    x =np.array(data)
    n,m =x.shape
    x_value = np.zeros([n,m])
    # print(n,m)
    for i in range(m):
        mean = np.mean(x[:,i])
        std = np.std(x[:,i])
        for j in range(n):
            x_value[j,i] = (x[j,i]-mean)/std
    return x_value
x_data = Standardize(x)
# x_data = pd.DataFrame(x_data).fillna(0)
print(x_data.shape)

