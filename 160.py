# python3.5/win10
# -*- coding:utf-8 -*-

'''
写一个函数fun(n)
fun(1)为1
fun(2)为1的2次方+2
fun(3)为(1的2次方+2)的2次方+3
以此类推。
'''

'''
递归，参数太大运算很慢
迭代
'''

'''
# 递归
def fun(n):
    if n == 1:
        return n
    result = fun(n-1)**2 + n
    return result          
'''

# 迭代
def fun(n):
    result = 0
    for i in range(1,n+1):
        result = result ** 2 + i
    return result

if __name__ == '__main__':
    for i in range(1,6):
        print("fun(%d)结果为%d" % (i,fun(i)))
    
    