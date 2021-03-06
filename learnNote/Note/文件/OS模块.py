import os
import shutil
# os.rename('Test.txt','Test重命名.txt') #重命名
# os.remove() #删除
# os.mkdir('f:/创建文件夹') #只能创建一级目录
# os.mkdirs('一级目录/二级目录') #创建多级目录
# os.rmdir('删除文件夹') #只能删除空目录
# shutil.rmtree('一级目录') #删除非空目录

# print(os.getcwd()) #获取当前目录
# print(os.path) #py路径
# print(os.path.join(os.getcwd(),'venv')) #路径拼接
# print(os.listdir('d:/')) #旧版获取一级目录列表

# with os.scandir('d:/') as entries: #现代版遍历目录
#     for entry in entries:
#         print(entry.name)

# basePath='d:/'
# for entry in os.listdir(basePath):
#     if os.path.isfile(os.path.join(basePath,entry)): #判断是否是文件
#         print(entry)


