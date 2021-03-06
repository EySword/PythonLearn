dictA = {'pro':'art','school':'NJU'}
'''
#添加内容
dictA['name'] = '李易峰'
dictA['age'] = 30
dictA['pos'] = 'singer'
'''

# print(len(dictA)) #一个键值对算一个长度
# print(dictA) #输出完整的字典
# print(dictA['pro']) #对应键获取相应值
# dictA["school"] = 'PKU' #可直接通过键修改
# print(dictA.keys()) #获取所有的键
# print(dictA.values()) #获取所有的值
# print(dictA.items()) #获取所有的键值对
# for i,j in dictA.items():
#     print('%s == %s'%(i,j))
# dictA.update({'school':'ZJU'}) #修改
# del dictA['pro'] #删除
# dictA.pop('pro') #删除
sorted(dictA.items(),key=lambda d:d[0]) #按照ask码排序
print(dictA)