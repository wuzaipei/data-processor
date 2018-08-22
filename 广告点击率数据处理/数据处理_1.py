# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取硬盘文件
# with open(r'H:\广告数据集---\kaggle-2014-criteo 数据集\kaggle-2014-criteo\train.txt') as f:
#     data = pd.read_table(f,header=0,nrows=100000)
# print(data.shape)
# data.to_csv('data/train_3.csv')

def sigmoid(x):
    import numpy as np
    x = np.array(x)
    n,m = x.shape
    data = np.zeros([n,m])
    for i in range(n):
        for j in range(m):
            data[i,j] = 1.0 / (1 + np.exp(-float(x[i,j])))
    return data


def read_txt(read_file_path_name,nrows,save_file_path_name):
    with open(read_file_path_name) as f:
        data = pd.read_table(f,header=None,nrows=nrows)
    print(data.shape) #查看文件大小
    # data = pd.get_dummies(data)
    # data_0 = data.iloc[:,0].reshape(-1,1)  # train数据才用到
    # print(data_0.shape)
    data_1 = sigmoid(data.iloc[:,:12])
    print(data_1.shape)
    data_2 = pd.get_dummies(data.iloc[:,13:-1])
    print(data_2.shape)
    data_train = np.hstack((data_1,data_2.values))
    pd.DataFrame(data_train).to_csv(save_file_path_name)
    return data_train #返回我们读取的文件 可用可不用 因为我们已经将它保存起来了

# 调用格式如下：
read_file_path_name = r'H:\蒋子龙给吴再培\kaggle-2014-criteo\PaxHeader\test.txt'
nrows = 1000
save_file_path_name = 'data_2/test_1.csv'
data = read_txt(read_file_path_name,nrows,save_file_path_name)

print(data.shape)
