import types

def dymicMrthod(self):
    print(self.name,self.school)
    pass

@classmethod
def classTest(cls):
    print('类方法')
    pass

@staticmethod
def staticMothod():
    print('静态方法')
    pass

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return '{}{}岁'.format(self.name,self.age)
    pass

XM=Student('XiaoMing',19)
XM.weight=100 #动态添加
Student.school='nju' #动态添加类属性
print(XM.weight)
XM.printInfo=types.MethodType(dymicMrthod,XM) #动态绑定方法

XM.printInfo() #调用动态绑定方法

Student.TestMethod=classTest #绑定类方法
Student.TestMethod()

Student.Static=staticMothod #绑定静态方法
Student.Static()