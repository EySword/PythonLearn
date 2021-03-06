class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('Animal eat!')
    def drink(self):
        print('dirnk!')

class cub:
    def chinai(self):
        print('chinai!')
    def eat(self):
        print('cub eat!')

class Dog(Animal): #单继承Animal父类
    def wang(self):
        print('wang!')

class Cat(Animal,cub):
    def __init__(self,name):
        Animal.__init__(self.name) #手动继承父类的属性
        # super().__init__(name) #自动找到父类并调用方法，假设有多个父类，就会按顺序逐个寻找
    def miao(self):
        print('miao!')


d1=Dog()
d1.eat()

c2=Cat()
c2.drink()
c2.chinai()

'''当多个父类存在相同方法的时候,按顺序逐层查找'''
c2.eat()
print(Cat.__mro__) #显示类的依次继承关系
