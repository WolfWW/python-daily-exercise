# python3.5/win10
# -*- coding:utf-8 -*-

'''
我们知道1的阶乘是1，2的阶乘是2，3的阶乘是6，4的阶乘是24，将前4个数字的阶乘排在一起是12624，现在要求将1~50的阶乘排在一起打印出来，要求，每40个数字1行，当本行超过40个时换行到下一行，另外在每行的开头打印行号。

'''


def factorial(i):
    result = 1
    for x in range(1,i+1):
        result = result * x
    return result
    
    
def join_fact(i):
    result = ''
    temp = []
    for x in range(1,i+1):    
        temp.append(str(factorial(x)))
        result = ''.join(temp)
    return result
    
    
def print_result(i):
    result = join_fact(i)
    count = len(result) // 40
    row = 1
    for x in range(count):
        print("(%2d)"%row,end=' ')
        print(result[x*40:(x+1)*40])
        row += 1
    print("(%2d)"%row,end=' ')
    print(result[count*40:])

if __name__ == '__main__':
    print_result(50)

