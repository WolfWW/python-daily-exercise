# python3.5/win10
# -*- coding:utf-8 -*-

'''
实现打印字母三角形，如:
fun(1)输出:
A
fun(2)输出
 A
ABA
fun(3)输出:
  A
 ABA
ABCBA
fun(28)最底层应为:
ABCDEFGHIJKLMNOPQRSTUVWXYZABAZYXWVUTSRQPONMLKJIHGFEDCBA
即当达到字母Z以后再从A开始。

'''

'''
分析题目有以下特点：
    1.不论正反，字母按顺序排列
    2.每一行相对最后一行都居中
    3.第n行就先打印前面n个字母，然后去掉第n个，反序打印

1.列表生成式，生成字母列表
2.居中显示，字符串center()方法
3.字符串连接
'''


import string

def fun(rows):

    upper_list = [letter for letter in string.ascii_uppercase][:rows]
    str = ''.join(upper_list)
    width = 2 * rows -1

    if rows > 26:
        str = str * (rows//26) + str[:rows%26]
        
    for i in range(rows):
        out_str = str[:i+1] + str[:i][::-1]
        print(out_str.center(width))

          

if __name__ == '__main__':
    while 1:
        rows = int(input("输入行数(0则退出)："))
        if rows == 0:
            exit(0)
        fun(rows)
        print('')
