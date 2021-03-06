#贪婪模式：
#默认的匹配规则
#在满足条件的情况下尽可能多地去匹配数据
import re

rs1=re.match('\d{6,9}','1234567890')
rs2=re.match('\d{6,9}?','1234567890')  #在相应规则后面加一个问号就是非贪婪
print(rs1.group())
print(rs2.group())