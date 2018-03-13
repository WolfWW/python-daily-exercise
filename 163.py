# python3.5/win10
# -*- coding:utf-8 -*-

'''
本次的题目难度也不大，我们知道python整数的除法不论是否能够整除，得到的都是浮点数，现在生成一个新的整数类，并且其除法“/”运算当结果为整数时得到整数，否则得到浮点数。

'''

class Devision():
    def __init__(self,devidend,devisor):
        self.devidend = devidend
        self.devisor = devisor
        self.result = self.devision()       
    
    
    def devision(self):
        try:
            remainder = self.devidend % self.devisor
            result = self.devidend / self.devisor
            if remainder == 0:
                result = int(result)
        except ZeroDivisionError:
            result = '0不能作为除数'
        return result
            

if __name__ == '__main__':
    devidend = 5                            # 被除数
    devisor = 1                             # 除数
    devison = Devision(devidend,devisor)
    print(devison.result)