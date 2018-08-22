# -*- coding:utf-8 -*-

import pandas as pd
import os

path = r'H:\蒋子龙给吴再培\Track2\track2'
lis = os.listdir(path)
print(lis)

x_train = []
for i in lis:
    if i.endswith('.txt'):
        with open(path + '\\' + i) as f:
            if i == 'training.txt' or i== 'userid_profile.txt':
                file_name = i.split('.')[0]
                data = pd.read_table(f,nrows=10000,header=None,index_col=None)
                x_train.append(data)
                print(data.shape,'\n',data.head())
            else:
                file_name = i.split('.')[0]
                data = pd.read_table(f, nrows=10000, header=None, index_col=0,sep='|')
                # xlabel = data.iloc[:,0]
                # data = data.iloc[:,1]
                # data.to_csv('data_3/%s'%i)
                # data1 = pd.read_table('data_3/%s'%i,header=None,index_col=0,sep='|')
                # x_train.append(data1)
                print(data.shape, '\n', data.head())

print(len(x_train))

