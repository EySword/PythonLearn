class Student(object):
    __slots__ = ('name','age') #只能添加这里说明了的类名称
    def __str__(self):
        return '{},{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='XIAOWANG'
xw.age=20
# print(xw.__dict__) #所有可以用的属性
print(xw.__slots__)
print(xw)

#继承关系
class subStydent(Student):

    pass

lb=subStydent()
lb.name='ln'
lb.asd=123 #子类不限制

print(lb.asd)