# python3.5/win10
# -*- coding:utf-8 -*-

'''
本次的题目难度也不大，我们知道python整数的除法不论是否能够整除，得到的都是浮点数，现在生成一个新的整数类，并且其除法“/”运算当结果为整数时得到整数，否则得到浮点数。

'''

'''
题目的本意就是复写除法方法
0为除数本身就是使用者的错误，不需要考虑
'''


class Nint(int):
    def __init__(self,num):
        self.num = num
    
    def __truediv__(self,other):
        return self.num // other if self.num % other == 0 else self.num / other
                        
    def __rtruediv__(self,other):
        return other // self.num if other % self.num == 0 else other /self.num
            

if __name__ == '__main__':
    a = Nint(12)
    b = Nint(9)
    c = Nint(4)
    print(a/c)
    print(b/c)
    print(b/3)
    print(10/c)
    print(0/c)