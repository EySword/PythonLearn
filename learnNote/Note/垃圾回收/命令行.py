# import sys
# print('参数个数为:',len(sys.argv),'个')
# print('参数列表:',str(sys.argv))
import argparse

#创建一个解析对象
parse=argparse.ArgumentParser(prog='文件名',usage='描述用途',
                              description='help信息前显示的信息',epilog='help信息后显示的信息')

#添加位置（必选）参数
parse.add_argument('name',type=str,help='你自己的信息')

#添加可选参数
parse.add_argument('-s','--sex',default='男',choices=['男','女'],help='你的性别')

# print(parse.print_help())

result=parse.parse_args() #开始解析参数
print(result)
