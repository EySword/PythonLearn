import os

data=open('./workerData.txt','r')

dataList=data.read().split(' ')
data.close()
nameNumber=int(len(dataList)/2)

newdata=open('./workerData.txt','w')

def inquire(name,data):
    pos1=data.index(name)
    print('{}的工资是{}'.format(name,data[pos1+1]))
    pass
def modification(name,data):
    newSalary=input('请输入新的工资：')
    if not newSalary.isdigit():
        print('请输入数字')
        return data
    pos2=data.index(name)
    data[pos2+1]=newSalary
    print('{}的工资已修改为{}'.format(name,newSalary))
    return data
def addWorker(name,data):
    newSalary = input('请输入新的工资：')
    if not newSalary.isdigit():
        print('请输入数字')
        return data
    data.append(name)
    data.append(newSalary)
    print('已添加{}，工资为{}'.format(name,newSalary))
    return data
def delWorker(name,data):
    pos4=data.index(name)
    data.pop(pos4)
    data.pop(pos4)
    print('{}已被删除'.format(name))
    return data
def notInList(name,data):
    if name not in data:
        return False
    else:
        return True

while True:
    fun = input('您想要做什么？1.查询员工工资 2.修改员工工资 3.增加新员工记录 4.删除员工信息 0.结束操作\n请选择：')
    if fun == '1':
        inputName1=input('请输入想要查询的员工姓名：')
        if notInList(inputName1,dataList):
            inquire(inputName1,dataList)
            pass
        else:
            print('姓名输入有误')
            pass
        pass
    elif fun == '2':
        inputName2 = input('请输入想要修改工资的员工姓名：')
        if notInList(inputName2, dataList):
            newList2=modification(inputName2,dataList)
            pass
        else:
            print('姓名输入有误')
            continue
        dataList=newList2
        pass
    elif fun=='3':
        inputName3 = input('请输入想要添加的员工姓名：')
        if notInList(inputName3, dataList):
            print('姓名已存在')
            continue
            pass
        else:
            newList3 = addWorker(inputName3,dataList)
            pass
        dataList=newList3
        pass
    elif fun== '4':
        inputName4 = input('请输入想要删除的员工姓名：')
        if notInList(inputName4, dataList):
            newList4 = delWorker(inputName4, dataList)
            pass
        else:
            print('姓名输入有误')
            continue
        dataList=newList4
        pass
    elif fun=='0':
        print('操作结束')
        break
    else:
        print('请正确输入...')

for each in dataList:
    newdata.write(each+' ')
    pass


newdata.close()

# os.remove()



