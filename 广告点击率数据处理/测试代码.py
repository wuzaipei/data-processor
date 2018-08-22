# -*- coding:utf-8 -*-

# a = 'nihao'
# b = '你好'
# d = 'good'
# c = [a,b,d]
#
# for i in c:
#     if i == 'nihao' or i=='你好':
#         print(i+' 成功')
#     else:
#         print(i+' 不成功')




# def np_max(x):
#     '''
#     x 的传参数一定的是numpy
#     :param x:
#     :return:
#     '''
#     import numpy as np
#     n, m = x.shape
#     max_values = np.zeros((1,1))
#     max_index = np.zeros((1,1))
#     max_columns = np.zeros((1,1))
#     if type(x) == type(np.random.random([1,1])):
#         max_values = np.max(x)
#         length = np.argmax(x)
#         max_index = length//m
#         max_columns = length%m
#     else:
#         print('请将数组的值通过 np.arry() 转为numpy类型')
#     return max_values,max_index,max_columns
#
# import numpy as np
# x = np.random.randn(5,4)
# print(x)
# print(np.max(x))
# max_values,max_index,max_columns = np_max(x)
# print(x[max_index,max_columns])

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# #
# f(3),f(3,[3,2,1]),f(2)
# import numpy as np
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(list(A0.values()))
# A1 = range(10)
# A2 = [i for i in A1 if i in list(A0.values())]
# print(A2)

# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]


# str = a
# resoult = {}
# for i in str:
#     resoult[i] = str.count(i)
# print(resoult)

# print(len(a))
# c = '1872490'
# d = '01233'
# x = []
# for i in range(len(a)):
#     for j in range(len(c)):
#         if a[i] == c[j]:
#             x.append(j)
# print(x)
#
# dianhua =[]
# for xi in x:
#     dianhua.append(c[xi])
#
# print(''.join(dianhua))


A='1872490'
phone = ''.join([A[[0,1,2,3,3,1,4,5,5,6,2][i]] for i in range(len([0,1,2,3,3,1,4,5,5,6,2]))])
# print(phone)

