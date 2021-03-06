import re

# | 竖线匹配左右任意一个表达式
str='wywasdqwerd888'
rs=re.match('(wywasdqwerd|wywasdqwerd888)',str)
print(rs.group()) #匹配到了就不会再往后找了

# (ab)将ab分为一个组
#匹配电话号码 xxxx-12335
# ^有两种含义：1、匹配开头 2、否定取反
rm=re.match('([0-9]*)-(\d*)','0355-31245455')
print(rm.group())
print(rm.group(1)) #group分组输出

# \num 引用分组num匹配到的字符串
htmlTag='<html><h1>测试数据</h1></html>'
ht=re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmlTag)
print(ht.group(1))
print(ht.group(2))
print(ht.group(3))
print(ht.group())

# (?P<name>)分组起名 (?P=name)使用名字
data='<div><h1>www.baidu.com</h1></div>'
a=re.match(r'<(?P<div>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=div)>',data)
print(a.group())