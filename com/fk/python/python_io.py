import os

# str = int(input("请输入一个数字"),10)
# print("您输入的数字大于10: %s" %(str > 10))

# open 函数
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 语法：
#
# file object = open(file_name [, access_mode][, buffering])
# 各个参数的细节如下：
#
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

file = open("/Users/fengkai/Desktop/rawdata", "r+")
print("文件名称：", file)

# file.write("this is my house")

# 读取文件按字节
print(file.readline(10000))

print("当前位置", file.tell())

print("继续读取", file.readline(100))
print("指针回到头部", file.seek(0, 0))
print("从头读取", file.readline(100))

# 关闭打开的文件
file.close()
print("文件名称：", file.mode)

# try catch语句
# try也可以嵌套执行
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败", fh)
else:
    print("内容写入文件成功")
finally:
    fh.close()
    print("finally执行成功")


def _raise_():
    if 0 < 1:
        raise Exception("try exception")


_raise_()



