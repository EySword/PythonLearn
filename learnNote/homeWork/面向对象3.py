import types
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __str__(self):
        return '姓名是{}，年龄是{}'.format(self.__name,self.__age)

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
        pass

    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age=age
        pass

    def JudjeAge(self):
        if self.__age>120 or self.__age<0:
            print('年龄设置不成功')
            pass
        else:
            print('年龄设置成功')

    name=property(getName,setName)
    age=property(getAge,setAge)
    pass

xm=Person('小明',18)
print(xm)
xm.name='小小明'
xm.age=9
print(xm)

class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super().__new__(cls)
            pass
        return cls._instance

    def __init__(self,name):
        self.name=name
        print(self.name)
        pass
    pass

A=Single(123)

class Animal:
    pass

def run(self):
    print('{}run'.format(self))
    pass

cat=Animal()
cat.color='blue'
cat.Run=types.MethodType(run,cat)

cat.Run()

@classmethod
def Print(self):
    print('ok')
    pass

Animal.pp=Print

Animal.pp()
