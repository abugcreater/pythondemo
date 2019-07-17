import sys
from math import cos



# 无参无返回函数
def hello():
    print("hello world!")
    print("and good morning good afternoon good night")


pass


def hello_name(name):
    print("hello%s" % (name))

    pass


def hello_no_param():
    return 1


def hello_param(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
        i += 1

    return sum

#可变函数
def hello2(*arg):
    print(arg)
    for name in arg:
        print("hello, %s" % (name))


pass

#关键字函数
def hello3(**kwargs):
    print('hello, %s' % kwargs['name'])
    print('you age: %s' % kwargs['age'])

    pass

#默认函数
def hello4(name = 'deam', age = 30):
    print("name:%s" %name)
    print("age:%s" %age)

pass


money = 2000

def changeMoney():
    #想对全局变量赋值必须加上global关键字
   global money
   money = 3000 + money

print(money)
changeMoney()
print(money)

print(hello_no_param())

print(hello_param(10))

hello2('adadsf', 'acfun', 'bilibili')

hello3(name='fuck',age=12)

hello4('dfd',89)


# 内名函数
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))


print(cos(0.5))


