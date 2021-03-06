'''
#打开文件
#默认编码是gbk，是中文编码
#打开文献时指定编码类型
fobj=open('./测试.txt','w')
#开始读写
fobj.write('在苍茫的大海上\n')
fobj.write('狂风卷积着乌云\n')
fobj.close()
'''
'''
#以二进制方式
fobj=open('Test.txt','wb') #str->bytes
fobj.write('在乌云和大海之间'.encode('utf-8'))
fobj.close()
'''
'''
fobj=open('测试.txt','a') #用于追加数据
fobj.write('在乌云和大海之间\n')
fobj.write('海燕像黑色的闪电\n')
fobj.close()
'''

#读取
# f=open('./测试.txt','r')
# print(f.read()) #读取所有数据,需要考虑光标
# print(f.read(12)) #读取12个数据
# print(f.readline()) #读一行
# print(f.readlines()) #读所有行
# print(f.readlines(1)) #只读一行
# f.close() #关闭文件对象

# with上下文管理
# with open('./测试.txt','r') as f:
    # print(f.read())
    # f.write('我觉得python非常好')

