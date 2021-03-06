#tell() 获取光标位置
# with open('测试.txt','r') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(4))
#     print(f.tell())

# #truncate() 对源文件进行截取操作
# fobjB=open('测试.txt','r')
# print(fobjB.read())
# fobjB.close()
# print('--------')
# fobjA=open('测试.txt','r+')
# fobjA.truncate(15)
# print(fobjA.read())
# fobjA.close()

#seek() 移动光标
with open('测试.txt','rb') as f:
    data=f.read(2)
    print(data.decode('gbk'))
    print(data.decode('gbk'))
    f.seek(-2,1)
    print(f.read(4).decode('gbk'))
