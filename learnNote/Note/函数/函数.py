def printName(name,age=21,):
    #name为必选参数，age为默认参数(但也可赋值)必须放在最后
    '''
    这里放函数提示，按ctrl显示
    :return:
    '''
    print('name is %s'%(name))
    print('age is %d'%age)

# printName('LiHua',22)

def fun1(*args):
    '''
    可选参数,为元组
    :param args:
    :return:
    '''
    print(args)

# fun1(1,2,3)

def fun2(**kwargs):
    '''
    关键字参数，类型为字典，key必须为字符串
    :param kwargs:
    :return:
    '''
    print(kwargs)
'''
dictA={'one':1,'two':2}
#下面是两种调用方法
fun2(**dictA) #需要**来传递
fun2(one=1,two=2)
'''
#可选参数必须在关键字参数之前

def Sum(a,b):
    sum = a+b
    return [sum,sum+1]

# print(type(Sum(2,4)))
# print(Sum(2,4))

pro=10
def ppro():
    '''
    修改全局变量
    :return:
    '''
    global pro
    pro=5
    print(pro)
ppro()
print(pro)

M=lambda x,y:x+y  #匿名函数
print(M(1,2))
max=lambda a,b:a if a>b else b   #双分支