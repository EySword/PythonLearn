class People:
    country='China'
    @classmethod #类方法所有权归类所有而不是实例对象
    def get_country(cls):
        return cls.country
        pass
    @classmethod
    def change_country(cls,data):
        cls.country=data #修改类属性
        pass
    @staticmethod #静态方法,主要用来存放逻辑性代码，本身没有与其他对象进行交互
    def getData():
        return People.country
    pass

print(People.get_country()) #通过类对象直接引用
print(People.getData()) #一般不用实例对象访问静态方法
