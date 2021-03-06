def SumNumber():
    print('输入数字，回车分割，以\#结束')
    number=[]
    inputN = 0
    Sum=0
    while inputN != '#':
        Sum += int(inputN)
        inputN=input()
    return Sum


print(SumNumber())
