import sys
import psutil
import os
import gc

def showMemSize(tag):
    pid=os.getpid()
    p=psutil.Process(pid)
    info=p.memory_full_info()
    memory=info.uss/1024/1024
    print('{} memory used:{} MB'.format(tag,memory))
# sys.getrefcount() 被引用的数量
a=[1]
b=a
print(sys.getrefcount(a))

#验证循环引用
def func():
    showMemSize('初始化')
    a=[i for i in range(10000)]
    b=[i for i in range(10000)]
    a.append(b)
    b.append(a)
    showMemSize('创建a,b后')
    pass

func()
showMemSize('完成后')
gc.collect()#手动释放内存
showMemSize('释放后')