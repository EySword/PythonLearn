try:
    # print(b) #捕获逻辑的代码
    # li=[1,2,3]
    # print(li[10])
    1/0
    pass
except NameError as msg:
# except:
    print('初次异常处理') #捕获到相应错误执行这里
    print(msg)
    pass
except IndexError as msg:
    print('初次异常处理')  # 捕获到相应错误执行这里
    print(msg)
    pass
except Exception as result:
    print(result) #万能捕获，但效率低
    pass
else:
    print('前面没有捕获到错误')
finally:
    print('不管怎么样出错都会执行')


