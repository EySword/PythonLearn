class Person: #类名
    name='小明' #属性
    age=20 #属性
    def eat(self): #方法
        # self.name='小明明'
        print('大口吃饭')
    def run(self): #方法
        print('飞快地跑')

Xiaoming=Person()
Xiaoming.sex='man' #添加属性
Xiaoming.eat() #调用函数
print(Xiaoming.name)

class People:
    def __init__(self,age): #这里的参数需要在调用类时赋值,是参数传递功能
        self.name='Xiaohong'
        self.age=age
        print('__init__的执行')

    def __str__(self):
        return '直接调用就会打印__str__里的内容,%s'%self.name

    def __new__(cls, *args, **kwargs):
        print('__new__的执行，只有这一句话时对象实例化不成功')
        return object.__new__(cls) #这是第一个是执行的函数，可以控制创建对象的一些属性限定，经常用来做单例模式的时候使用




XiaoLiang=People(18)
# print(XiaoLiang.age)
print(XiaoLiang)

'''魔术方法'''
'''
__init__:初始化一个类，在创建实例对象为其赋值时使用
__str__：在将对象转换成字符串对象的时候，打印对象的信息
__new__：创建并返回一个实例对象，调用了一次就会得到一个对象
__class__：获得已知对象的类（对象._class__）
__del__：对象在程序运行结束后进行对象销毁的时候调用这个方法来释放资源
'''