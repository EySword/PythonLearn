def DicProcess(inDic):
    '''
    将字典中长度大于2的值变为2个长度
    :param inDic: dic
    :return: dic
    '''
    for key,value in inDic.items():
        # print(keyyy,value)
        if len(value)>2:
            inDic[key]=value[0:2]
    return inDic

Dic={1:[1,2,3,4,5],2:"two"}

print(DicProcess(Dic))