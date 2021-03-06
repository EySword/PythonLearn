import re

data='Python is the best language'
result=re.match('P',data,re.I|re.M) #精确匹配 第三个参数表示忽略大小写
res=re.match('(.*) is (.*?) .*',data,re.I|re.M)
print(type(result))
print(result.group())
print(res.group(1))
print(res.group(2))
print(res.groups())

#re.compile re模块中的编译方法，可以吧字符串编译成字节码
#优点：在使用正则表达式进行match操作时，python会将字符串转为正则表达式对象，如果使用compile，只需要一次
reobj=re.compile('\d{4}')
rs=reobj.match('12345678')
print(rs.group())

#re.search 在全文中匹配一次，匹配到就返回
data2='我和我的祖国，一刻也不能分离'
rs2=re.search('不能',data2)
print(rs2) #索引范围,左闭右开
print(rs2.group())

#re.findall 匹配所有返回一个列表
data3='华为是华人的骄傲'
rs3=re.findall('华',data3)
print(rs3)

#re.sub(查找内容,替换成的内容,字段)
#re.subn() 与上同，还以元组形式返回被替换的数量
data4='Python is good'
rs4=re.sub('Python','C++',data4)
print(rs4)

#re.split 实现分隔字符串
data5='百度,腾讯,华为,阿里'
print(re.split(',',data5))