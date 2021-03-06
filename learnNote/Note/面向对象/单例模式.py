class Animal:
    def __init__(self):
        self.color='red'
        pass
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls,*args,**kwargs) #不重写new的时候默认是这样的
    pass

class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        # cls._instance=super().__new__(cls, *args, **kwargs)
        #不能用自身的new方法cls.__new__，会造成深度递归，应该调用父类的new方法
        if not hasattr(cls,'_instance'): #如果不存在就开始创建
            cls._instance = super().__new__(cls) #object调用__new__方法的时候是不需要任何参数
        return cls._instance
    def __init__(self,name):
        self.name=name
        # print(self.name)
    pass

db1=DataBaseClass(123)
print(db1.name)
db2=DataBaseClass(321)
print(db1.name)
print(db2.name)
print(id(db1))
print(id(db2))