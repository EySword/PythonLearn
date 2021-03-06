class Person:
    def __init__(self):
        self.__age = 18
        pass
    def get_age(self):
        return self.__age
        pass
    def set_age(self,age): #外部修改私有实例属性
        self.__age=age
        pass
    age=property(get_age,set_age) #定义一个类属性，实现通过直接访问类属性的形式去访问私有属性
    '''
    方法二：修饰器
    def __init__(self):
        self.__age = 18
        pass
    @property #getter方法
    def get_age(self):
        return self.__age
        pass
    @age.setter #setter方法
    def set_age(self,age): #外部修改私有实例属性
        self.__age=age
        pass
    '''
    pass
p1=Person()
print(p1.age)

