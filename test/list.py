# 生成1到10的数组：
ss = [value ** 2 for value in range(1, 11)]
# print (ss)
# 查找列表中的最大最小值，并找出他们的索引值
dd = [1, 2, 5, 64, 21, 5, 96, 0, 56, -2, 154, 11]
# print(min(dd))
# print(max(dd))
# print(dd.index(max(dd)))
# print(dd.index(min(dd)))
# 输出列表的长度
# print(len(dd))
# 通过传统的for循环求列表中所有元素相加的和
cc = [val for val in range(1, 1000001)]
# print(min(cc))
# print(max(cc))
# total=0
# for i in cc:
#     total+=i
# print(total)
# 通过sum函数直接对列表求和
# print(sum(cc))

# range(start,stop,step) 一个参数：表示从0开始生成到第一个参数结束，不包含该参数；
#                        两个参数：表示从第一个参数开始到第二个参数结束，不包含第二个参数；
#                        三个参数：第三个参数表示步长，不输入默认为1
ff = [va for va in range(1, 21, 2)]
# print(ff)
tt = []
# for va in range(3,31):
#     if va%3==0:
#         tt.append(va)
#         print(va)
# print(tt)

# n**m表示n的m次方
gg = [va ** 3 for va in range(1, 11)]
# print(gg)
# 切片[n:m] 从n开始m结束，不包含m表示从n开始到结束，不包含n表示从0开始到m结束
# 负数索引返回离列表结尾相应距离的元素[-3:]表示返回列表最后三个
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# 复制列表，而不是赋值
hobby = ['read', 'singing', 'shopping']
xmhobby = hobby[:]
hobby.append('running')
xmhobby.append('swiming')
# print(hobby)
# print(xmhobby)
# 空数组在python中为false，js中为false
pl = []
# if pl:
#     print('yes')
# else:
#     print('no')
# 需求：客户需要一些东西，可用的是另外一些东西，需要据此判断是否能满足客户需求
request_list = ['bread', 'banana', 'apple', 'tomato', 'pear']
available_list = ['apple', 'peach', 'tomato', 'grape', 'pear']
# for things in request_list:
#     if things in available_list:
#         print('yes,we have '+things+'.')
#     else:
#         print('sorry,there is no '+things+'.')

administrators = ['admin', 'zhangsan', 'Jhon', 'Havr', 'Yean']


# for ads in administrators:
#     if ads=='admin':
#         print('Hello admin, would you liketo seeastatus report?')
#     else:
#         print('Hello '+ads+', thank you for logging in again。')

# 需求，输入用户名，除了admin,其他都是一样的回应
def login():
    name = input('please input your username:')
    if name == 'admin':
        print('Hello admin, would you liketo seeastatus report?')
    else:
        print('Hello ' + name + ', thank you for logging in again。')
# login()