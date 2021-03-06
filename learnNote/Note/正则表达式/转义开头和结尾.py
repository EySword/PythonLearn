import re

print(re.match('c:\\\\a.txt','c:\\a.txt').group())
print(re.match(r'c:\\a.txt','c:\\a.txt').group()) #在正则前面加r，表示原生字符串

# ^匹配字符串开头
res1=re.match('^P.*','Python is a language')
if res1:
    print(res1.group())

# $匹配结尾
res2=re.match('[\w]{5,15}@[\w]{2,3}.com$','Python@qq.com')
if res2:
    print(res2.group())