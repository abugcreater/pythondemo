import sys
import time


sys.getdefaultencoding()
_t_ = time.clock()
print(_t_)

#list数据格式,列表元素有序,不需要都是同一种元素
a = [1,2,3]
b = ['1',2,None]
c = [1,2,[3,4]]
d = []
#用于切片list[start_index:end_index:step_length]
#start_index开始下标省略时，默认为 0 ；end_index结束下标省略时，默认为最大下标，及长度-1或-1；step_length步长省略时，默认为1。
e = [1,2,3,4,5,6,7,8,9,0]
print(a, b, c, d)

e = e[6:10:1]

a[2] = 'sdfdf';
print(a,e,len(a))
#列表联合符号为+, reversed，切片反转列表
print(a + c, list(reversed(a)), a[::-1])
print(dir(list))

#元组tuple，元素不可修改
_a = (1,2,3,3,4)
print(type(_a),_a*2)

#字典dict，键值对,多个直接覆盖；集合其中元素不可重复
_map_a = {'name':'fuck',"age":12,'name': 'shit'}
_map_a['address'] = 'los angeles'
del _map_a['age']
print(_map_a.get('name',''), dict(name='Tim', age=18), {(1,2):'Time'},_map_a['name'], _map_a)

_set_s = {'1','2','4','3'}
print(_set_s, type(_set_s))

''''
序列
序列(sequence)，在Python中是一种具有相同特性的高级数据结构的统称，可以使用下标来获取元素和切分。
到现在，我们学习了列表、元组、字典和集合4种高级数据结构。可以发现，列表和元组在操作上有许多相同的地方。
除了列表和元组，还有字符串也是序列。可见列表、元组、字符串为序列，字典、集合、数值为非序列。
'''''


'''
可变类型（mutable）：列表，字典，集合；
不可变类型（unmutable）：数字，字符串，元组；
'''
n4 = n3 = n2 = n1 = "123/'Wu'"

_n1 = {"k1": "wu", "k2": 123, "k3": ["alex", 456]}
_n2 = _n1



