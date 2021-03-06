import pygame
import random
import time
from pygame.locals import *

'''
1、实现飞机的显示、控制
'''
class HeroPlane(object):
    def __init__(self,screen):
        '''

        :param screen: 主窗体对象
        '''
        #飞机默认位置
        self.x=206
        self.y=500
        #设置要显示内容的窗口
        self.screen=screen
        #生成图片
        self.image=pygame.image.load('./picture/AF.png')
        self.bulletList=[]
        pass
    def moveLeft(self):
        if self.x>0:
            self.x-=10
            pass
        pass
    def moveRight(self):
        if self.x<412:
            self.x+=10
            pass
        pass
    def moveUp(self):
        if self.y>0:
            self.y-=10
            pass
        pass
    def moveDown(self):
        if self.y<567:
            self.y+=10
            pass
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        #完善子弹的展示逻辑
        needDelItemList=[]
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display() #显示子弹的位置
            bullet.move()
        pass
    def shootBullet(self):
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
        pass

class EnemyPlane:
    def __init__(self,screen):
        #设置默认方向
        self.direction='right'
        # 飞机默认位置
        self.x = 20
        self.y = 10
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成图片
        self.image = pygame.image.load('./picture/EF.png')
        self.bulletList=[]
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()
        pass
    def shootBullet(self):
        """
        随机发射子弹
        :return:
        """
        num=random.randint(1,100)
        if num==3:
            newBullet=enemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        if self.direction=='right':
            self.x+=1
            pass
        elif self.direction=='left':
            self.x-=1
            pass
        if self.x>412-40:
            self.direction='left'
            pass
        elif self.x<40:
            self.direction='right'
            pass
    pass

def keyControl(HeroObj):
    eventList=pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('exit')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveLeft()
                pass
            if event.key == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveRight()
                pass
            if event.key == K_w or event.key == K_UP:
                print('up')
                HeroObj.moveUp()
                pass
            if event.key == K_s or event.key == K_DOWN:
                print('down')
                HeroObj.moveDown()
                pass
            if event.key == K_SPACE:
                print('shoot')
                HeroObj.shootBullet()
                pass

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x=x+25
        self.y=y
        self.screen=screen
        self.image=pygame.image.load('./picture/AB.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=5
        pass
    def judge(self):
        '''
        判断子弹越界
        :return:
        '''
        if self.y<0:
            return True
        else:
            return False
        pass
    pass

class enemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x+25
        self.y=y
        self.screen=screen
        self.image=pygame.image.load('./picture/EB.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y+=2
        pass
    def judge(self):
        '''
        判断子弹越界
        :return:
        '''
        if self.y>567:
            return True
        else:
            return False
        pass
    pass

def main():
    #创建窗口对象
    screen=pygame.display.set_mode([412,567],0,32)
    #设定背景图片
    background=pygame.image.load('./picture/BG.png')
    #设置标题
    pygame.display.set_caption('飞机小游戏')

    #添加bgm
    pygame.mixer.init()
    pygame.mixer.music.load('./picture/Dmitri Shostakovich - VI. Waltz 2 from Jazz Suite No. 2 (Eyes Wide Shut).mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1) #无限循环

    #载入玩家的飞机
    hero=HeroPlane(screen)
    #创建敌机
    enemy=EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()#显示玩家飞机
        enemy.display()#显示敌机
        enemy.move()
        enemy.shootBullet()
        #获取键盘事件
        keyControl(hero)
        #更新显示内容
        pygame.display.update()
    pass


if __name__=='__main__':
    main()