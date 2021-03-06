class Fruit:
    def __init__(self,color):
        self.color=color

apple=Fruit('red')
print(apple.color)

class Animal:
    def __init__(self,color,name,age):
        self.color=color
        self.name=name
        self.age=age

    def run(self):
        print('run')


    def eat(self):
        print('eat')

    def __str__(self):
        return '%s,%s,%s'%(self.name,self.color,self.age)

lion=Animal('yellow','lion','age')
print(lion)