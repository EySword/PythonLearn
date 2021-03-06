#数值运算函数
print(1.1,abs(-10),'绝对值')
print(1.2,round(1.123456,3),'对浮点数保留小数')
print(1.3,pow(2,5),'2的5次方')
print(1.4,max([1,2,3,4,5,4,3,2,1]),'取序列最大值')
print(1.5,sum(range(10),5),'序列求和，第二个参数为初始值')
print(1.6,eval('a+b+c',{'a':1,'b':2,'c':3}),'动态执行字符串表达式,后面参数声明必须是字典类型')

#类型转换函数
# int() float() str()
print(2.1,bin(10),'转换为二进制')
print(2.2,oct(10),'转换为八进制')
print(2.3,hex(10),'转换为16进制')
print(2.4,bool(0),'转换为布尔类型，0、空。False为False')
print(2.5,chr(65),'以0-255范围内整数为参数，返回对应的ascii字符')
print(2.6,list((1,2,3,4,5)),'将元组转换为列表')
print(2.7,tuple([1,2,3,4,5]),'将列表转换为元组')
print(2.8,dict(a=1,b='two',c=True),'生成字典')
print(2.9,bytes('我爱你',encoding='utf-8'),'转换为字节数组')

#序列操作函数
print(3.1,all(['',1,2,3,4]),'判断可迭代对象是否都为True')
print(3.2,any(['',1,2,3,4]),'判断可迭代对象是否全为False，有一个为True就为True')
print(3.3,sorted((2,4,3,1,5,2),reverse=True),'对所有可迭代对象排序,True为降序，False为默认升序。sort方法是原基础上改动，sorted是生成新的list')
#range(起始，终止，步长）
print(3.4,list(zip((1,2,3,4),('one','two','three'),['你','我'])),'将参数对应位置打包成元组，返回由这些元组组成的列表')
print(3.5,list(enumerate({1:'one',2:'two'},4)),'将可遍历对象组合为一个索引序列，第二个参数为索引起始位置')

#集合操作函数
set1={1,2,3}
set2={2,3,4}
set1.add('one')
# set1.clear()
print(set1.difference(set2)) #取差集
print(set2-set1) #取差集
print(set1.intersection(set2)) #取交集
print(set1.union(set2)) #取并集
print(set1|set2) #取并集
print(set1.pop()) #随机移除某个元素并获得这个元素
print(set1.discard(2)) #指定移除但不获得
print(set1.update(set2)) #原集合基础上进行更新
print(set1)