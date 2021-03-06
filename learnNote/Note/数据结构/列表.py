'''
li = [1,2,3,'你好']
print(len(li))
print(type(li))
'''
listA=['qwdqas',12,1.3,True]
print(listA)
'''
# 查找
print(listA) #输出完整的列表
print(listA[0]) #输出第一个元素
print(listA[1:3]) #输出第2,3个元素
print(listA[::-1]) #倒序输出
print(listA*2) #列表数据翻倍
'''
'''
listA.append(['asd',False]) #追加嵌套列表
listA.append(123) #追加内容
listA.insert(1,'1后') #在指定位置插入
listB = list('range(10)') #强制转换list
listA.extend(listB) #批量添加
listA.extend([1,3])
'''
'''listA[0]=31 #可直接修改
# del listA[0:3:2] #删除指定/批量位置
listA.remove(12) #移除指定元素 数据值！
listA.pop(0) #移除指定位置 索引值！
print(listA.index(12))  #查找数据 index(查找内容,开始下标,结束下标）'''
print(listA)

#共有方法 + * in 对于字符串、列表、元组都适用
strA='abc'
strB='123'
print(strA+strB)
print(strA*3)
print('b'in strA)
dicA={'1':3}
dicB={'2':4}
print(1in dicA)