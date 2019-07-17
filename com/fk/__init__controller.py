# Python中的if else等条件控制语句

import sys
import time

_a = time.clock()

# 当if单独使用时时相当于Java中的switch case；如果后边跟了布尔值在表示条件判断
if _a > 0:
    print("_a > 0", _a)
elif _a == 0:
    print("_a is so weak", _a)
else:
    print("the break")

if '1':
    print("aaa")
if '2':
    print('bbbb')
else:
    print('what`s you problem')

#三元操作符
now_time = time.clock()
a = '上午好' if now_time < 12 else '下午好'
print(a, now_time)


# 关于for操作
l = [1,2,3,4,5]
sum = 0
for i in l :
    sum += i
    sum +=1
print(sum)

l = [(1,2),(1,3),(1,4)]
for i, j in l:
    i == j
    # print(i)
    # print(j)

sum = 0
for i in range(1,6):
    sum += i
print(sum)


#break的运用
# while 中使用
sum = 0
while True:
    if sum > 10:
        print('sum已大于10')
        break
    sum += 1
    # print(sum)

# for 中使用
sum = 0
for i in range(100):
    if sum > 10:
        print('sum已大于10')
        break;
    sum += 1
    # print(sum)

for i in range(5):
    print(i)
    pass # 占位
