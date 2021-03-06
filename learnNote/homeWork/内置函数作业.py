def SumNumber():
    '''
    求出1-10,20-30和35-45的和
    :return:
    '''
    print('1到10的和',sum(range(1,11)))
    print('20到30的和',sum(range(20,31)))
    print('35到45的和',sum(range(35,46)))

def MonkNumber(monk=100,bun=100,big=3,smail=1/3):
    '''
    100和尚100馒头，大和尚3馒头，3小和尚1馒头。大小和尚各有多少？
    :return:
    '''
    mid=big-smail
    smailNumber=int((monk*big-bun)/mid)
    bigNumber=int(monk-smailNumber)
    print('大和尚有{}个'.format(bigNumber))
    print('小和尚有{}个'.format(smailNumber))

def FindSolo(TextLis=[1,3,2,45,2,7,54,23,1,45,7,54,23]):
    '''
    找出列表中独一无二的数字
    :param TextLis:
    :return:
    '''
    SortList=sorted(TextLis)
    Lenth=len(SortList)
    SortList.append(SortList[Lenth-1]+1)
    SoloList=[]
    for i in range(1,Lenth):
        if SortList[i] == SortList[i-1]:
            SoloList.append(SortList[i-1])
        else:
            continue
    print('独一无二的数字是',list(set(TextLis)-set(SoloList))[0])

SumNumber()
MonkNumber()
FindSolo()