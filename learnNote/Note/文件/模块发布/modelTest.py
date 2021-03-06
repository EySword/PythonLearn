def add(x,y):
    return x+y

def ddf():
    print('测试函数')

__all__=['add'] #可作为模块调用的范围

#模块内部的测试代码
if __name__=='__main__':
    ddf()
    print(add(2,4))
    print('模块__name__变量=%s'%__name__)