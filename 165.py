# python3.5/win10
# -*- coding:utf-8 -*-

'''
打印中文乘法口诀表：
一一得一    
一二得二    二二得四    
一三得三    二三得六    三三得九   
...
用循环或等同循环的方法
'''

'''
分析题目：
1.数字转汉字需要拆分后一一对应
2.口诀表中所有的汉字只有一到十
3.个位直接换，0不输出
4.十位模10后转换为结果+’十'
5.为了对齐，可以每一个打印用str.center(width)居中
'''


def int_to_cn(i,j):
    num_dict = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十'}

    result = j * i
    tens = result // 10
    units = result % 10
    tens_cn = ''
    units_cn = ''
    if tens:
        tens_cn = num_dict[tens] 
    if units:
        units_cn = num_dict[units] 
    if tens:
        result_cn = num_dict[j] + num_dict[i] + tens_cn + '十' + units_cn
    else:
        result_cn = num_dict[j] + num_dict[i] + '得' + units_cn
    return result_cn

if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            result_cn = int_to_cn(i,j)
            print(result_cn.center(8),end='') if len(result_cn)==4 else print(result_cn.center(7),end='')      
        print('')
    
    