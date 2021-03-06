class ToolongMyException(Exception):
    def __init__(self,leng):
        self.leng=leng
        pass
    def __str__(self):
        return 'Error Leng'
    pass

def name_Text():
    name=input('请输入：')
    try:
        if len(name)>3:
            raise ToolongMyException(len(name))
        else:
            print(name)
            pass
        pass
    except ToolongMyException as result:
        print(result)
        pass
    pass

name_Text()