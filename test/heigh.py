from functools import reduce

# *args 是用来发送一个非键值对的可变数量的参数列表给一个函数
def test(*args):
    for arg in args:
        print('  the has  ' + arg)


# test('sdad','ddsf','gasd')

# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数

def testMore(**kwargs):
    for key, value in kwargs.items():
        print('{0}==>{1}'.format(key, value))


a = {
    'name': '张三',
    'age': '10',
    'sex': 'male'
}


# testMore(**a)

# 迭代器
class Lab():
    def __init__(self):
        self.books = ['ad', 'cd', 'sd']

    def tell(self):
        it = iter(self.books)
        print(next(it))
        print(next(it))
        print(next(it))
ll = Lab()
# ll.tell()

def foo():
    print("starting...")
    while True:
        # 第一次 yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作
        res = yield 4
        print("res:",res)
g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))
# print("*"*20)
# print(g.send(7))
# starting... 是函数运行结果，直接输出
# 4           是第一次print(next(g)) 输出的结果，直接return了，没有赋值操作
# *********** 是第一次结束后的print("*"*20)
# res:Nome    从第一次yield return后开始执行，第一次yield已经return了4，这次后边为空，所以res = None
# 4           yield执行没有完，while循环，执行yield 4又一次return 4，print(next(g))打印出 4
# *********** 是第二次结束后的print("*"*20)
# res:7       第二次return 4 res等式右边为None，但是send(7),将7赋值给res,此时就执行了，print("res:",res)
# 4           第三次函数循环 return 4

def appendAll(list):
    ary = []
    for i in list:
      if i%2 == 1:
          ary.append(i * 2)
      else:
          ary.append(i ** 2)
    return ary

ad = appendAll([1,2,3,4])
# print(ad)

# Map函数使用
def mapfuns(lists):
    return list(map(lambda x:x**2,lists))

# print(mapfuns([1,2,3,4]))
# map用于函数

def multipy(x):
    return x*x
def add(x):
    return x+x
funs = [multipy,add]
# range返回的是一个可迭代对象,list将可迭代对象转化为列表，
# x为可迭代对象range(5),x(i)表示可迭代对象的第i个元素
for i in range(5):
    a = list(map(lambda x:x(i),funs))
    print(a)

# filter过滤器
def filtfuncs():
    a =[]
    b=range(-5,5)
    a = list(filter(lambda x:x<0,b))
    return a
# print(filtfuncs())


# reduce 工具包里的函数，简化运算
# 求列表的阶乘
def multMore(lis):
    return reduce((lambda x,y:x*y),lis)
print(multMore([1,2,3,4]))
# set 数据结构

class SetFunc:
    def __init__(self,some_list):
        self.some_list=some_list
    def tradition(self):
        '''去掉列表中的重复项'''
        d=[]
        for x in self.some_list:
            if x not in d:
                d.append(x)
        return d
    def moreThanOne(self):
        '''列表中出现次数大于一的元素'''
        d=[]
        for x in self.some_list:
            if self.some_list.count(x)>1:
                if x not in d:
                    d.append(x)
        return d
    def useSet1(self):
        '''使用set函数去掉列表中重复的元素'''
        d=[]
        d= set([x for x in self.some_list if x not in d])
        return  d

    def useSet2(self):
        '''使用set函数返回列表中出现次数大于1的元素'''
        d=[]
        d = set([x for x in self.some_list if self.some_list.count(x)>1])
        return list(d)
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
y=SetFunc(some_list)
# print(y.useSet2())

class Person:
    pass