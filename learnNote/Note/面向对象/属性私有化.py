class Person:
    def __init__(self):
        self.__name='李四' #两个下划线私有化属性,不能在外部访问
        self.age=30
        pass
    def __str__(self):
        return self.__name #在内部访问
    def __eat(self): #私有化函数
        print('吃')
    pass

class Student(Person):
    pass #私有属性不能通过子类继承


xl=Person()
print(xl)  #是通过类属性外部访问的
stu=Student
