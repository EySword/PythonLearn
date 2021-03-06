class Animal:
    def __init__(self,name):
        self.name=name
        print('构造初始化方法')

    def __del__(self):
        print('当后面再没有任务的时候，解释器会自动调用此函数 来释放内存空间')
        print('对象被删除时也会调用')
        print('这是析构方法')


cat=Animal('小花猫')
del cat
input('程序等待中...')

# dog=Animal('柯基')
# input('程序再次等待')

