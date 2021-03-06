#文件备份
def copyFile():
    #接收文件名
    old_file=input('请输入文件名：')
    file_list=old_file.split('.')
    #构造新文件名
    new_file=file_list[0]+'_备份.'+file_list[1]
    old_f=open(old_file,'r') #打开文件
    new_f=open(new_file,'w') #准备写入新文件
    content=old_f.read() #读取
    new_f.write(content)
    old_f.close()
    new_f.close()
    pass

def copyBigFile():
    #接收文件名
    old_file=input('请输入文件名：')
    file_list=old_file.split('.')
    #构造新文件名
    new_file=file_list[0]+'_备份.'+file_list[1]
    try:
        with open(old_file,'r') as old_f,open(new_file,'w') as new_f:
            while True:
                content=old_f.read(1024) #一次读1024个数据
                new_f.write(content)
                if len(content)<1024:
                    break
    except Exception as msg:
        print(msg)

    pass