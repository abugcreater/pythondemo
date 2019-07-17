# coding:utf-8
import keyword
import sys
import math

keyword.kwlist
# 关键字
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try',
 'while', 'with', 'yield']
# 单行注释
'''
多行注释
'''
"""
多行注释
"""

name = 'dddd'  # 弱类型
print(keyword.iskeyword('and'), name, 12434, '5342523' + '314')
print('hello, world!' * 2)
_a = 'I\'m DeanWu!'
a_cha = '你好'
print(type(name), _a, sys.getdefaultencoding(), len(a_cha), a_cha[1], name[0:2], 'd' in name)
_b = 'suck my dick'
s = '%s,%s!' % (_a, _b)
d = '{1}，{0}'.format('世界', '你好')
print(s, d, dir(_a), not True)
# radius = float(input('请输入：'))
# perimeter = 2 * math.pi * radius
# print('圆的周长为:%.2f' %perimeter  )
year = int(input('请输入年份: '))
is_leap = ((year % 4 == 0 and year % 100 != 0) or
           year % 400 == 0)
print(is_leap)