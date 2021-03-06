import time

class Role:
    def __init__(self,name,hp):
        '''
        构造初始化函数
        :param name:姓名
        :param hp: 血量
        '''
        self.name=name
        self.hp=hp

    def tong(self,enemy):
        enemy.hp-=10
        info='[%s]捅了[%s]一刀'%(self.name,enemy.name)
        print(info)
    def kanren(self,enemy):
        enemy.hp-=15
        info = '[%s]砍了[%s]一刀' %(self.name, enemy.name)
        print(info)
    def chiyao(self):
        info='[%s]吃了一颗回血药'
        print(info)
    def __str__(self):
        return '%s的血量现在为%d'%(self.name,self.hp)

XMCX=Role('西门吹雪',100)
YGC=Role('叶孤城',100)

# XMCX.tong(YGC)
# print(YGC)
# print('================')
while XMCX.hp>0 and YGC.hp>0:
    a=input('选择一个人, A.XMCX B.YGC\n:')
    behave = input('想要他干什么? A.捅人 B.砍人 C.回血\n:')
    if a=='A':
        if behave == 'A':
            XMCX.tong(YGC)
        elif behave == 'B':
            XMCX.kanren(YGC)
        elif behave == 'C':
            XMCX.chiyao()
        else:
            continue
    elif a=='B':
        if behave == 'A':
            YGC.tong(XMCX)
        elif behave == 'B':
            YGC.kanren(XMCX)
        elif behave == 'C':
            YGC.chiyao()
        else:
            print('请正确输入')
            continue
    else:
        print('请正确输入')
        continue
    print(XMCX)
    print(YGC)
    print('========回合结束========')
    time.sleep(1)
