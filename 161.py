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
1.列表生成式
2.居中显示
3.字符串连接
'''


import string

def fun():
    rows = int(input("输入行数(0则退出)："))
    if rows == 0:
        exit(0)
    upper_list = [letter for letter in string.ascii_uppercase][:rows]
    str = ''.join(upper_list)
    width = 2 * rows -1

    if rows > 26:
        str += str[:rows-26]
        
    for i in range(rows):
        out_str = str[:i+1] + str[:i][::-1]
        print(out_str.center(width))
    
    print('')
    fun()
          

if __name__ == '__main__':    
    fun()