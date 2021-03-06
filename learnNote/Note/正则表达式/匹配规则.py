import re
'''
#.的使用 匹配任意一个字符
data='aaaa'
names='李达','李明','小王','小李'
pattern='李.'  #匹配规则
parrtern='..'  #匹配规则
for name in names:
    res = re.match(pattern, name)
    if res:
        print(res.group())
# res=re.match(parrtern,data)
# print(res.group())

#[]的使用 匹配中括号中任意一个字符
str1='eHello'
res=re.match('[he]',str1) #[a-z]表示从a到z
print(res.group())

#\d 匹配一个数字0-9
data='12345abcd'
print(re.match('\d\d',data).group())

#\D 匹配非数字
data2='ABC12345abcd'
print(re.match('\D',data2).group())

#\s 匹配空格、tab(4个\s)，\S是非空白
data3='     ABC12345abcd'
print(re.match('\s\s',data3).group())

#\w 匹配单词字符，即a-z,A-Z,0-9、_(下划线也包括)  \W匹配非单词字符
'''

