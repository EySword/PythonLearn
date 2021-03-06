import random
# # 随机整数：
# print random.randint(1,50)
# # 随机选取0到100间的偶数：
# print random.randrange(0, 101, 2)
# # 随机浮点数：
# print random.random()
# print random.uniform(1, 10)
# # 随机字符：
# print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
# # 多个字符中生成指定数量的随机字符：
# print random.sample('zyxwvutsrqponmlkjihgfedcba',5)
# # 从a-zA-Z0-9生成指定数量的随机字符：
# ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
# print ran_str
# # 多个字符中选取指定数量的字符组成新字符串：
# print ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
# # 随机选取字符串：
# print random.choice(['剪刀', '石头', '布'])
# # 打乱排序
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print random.shuffle(items)

age = random.randint(1,10)
GameNumber = 1
print (age)
result = True
while result:
    print("第%d次游戏开始！"%(GameNumber))
    for i in range(1,4):
        GuessAge = int(input("请输入你猜的年龄:"))
        if GuessAge == age:
            print('恭喜你！在第%d次游戏中猜了%i次猜中了年龄！'%(GameNumber,i))
            break
        elif i<3:
            print("猜错啦，你还有%d次机会"%(3-i))
        else:
            print("猜错啦，你没有机会了！")
    rightAnswer = 1

    while rightAnswer == 1:
        answer = input("你还想猜一遍吗？回答\'Y\'或者\'y\'是想，\'N\'或者\'n\'是不想\n"
                       "你的回答：")
        if answer == 'y' or answer == 'Y':
            print('欣赏你不服输的精神~')
            result = True
            rightAnswer = 0
        elif answer == 'n' or answer == 'N':
            print('那再见咯~')
            result = False
            rightAnswer = 0
        else:
            print('别调皮输入别的东西!\n'
                  '再问你一遍',end='')

    GameNumber+=1

