UnDone = eval(input('输入元组或者字符串:'))
#eval:执行字符串表达式，并返回表达式的值
def Cut(a):
    longth = len(a)
    #print(longth)
    b=[]
    for i in range(longth):
        #print('%d & %d'%(i,a[i]))
        if i%2 == 0:
            #print('这里%d'%i)
            b.append(a[i])

    return b

print(Cut(UnDone))
