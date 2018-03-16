# python3.5/win10
# -*- coding:utf-8 -*-

'''
元音字母 有：a，e，i，o，u五个， 写一个函数，交换字符串的元音字符位置。
假设，一个字符串中只有二个不同的元音字符。
二个测试用例：
输入 apple  输出 eppla
输入machin  输出 michan
不符合要求的字符串，输出None，比如：
输入 abca （两个元音相同） 输出 None
输入 abicod （有三个元音） 输入None

'''

'''
分析题目：
1.字符串有3个以上元音就None
2.字符串有2个相同元音就None
3.字符串没有元音输出None
4.元音数为2且是不同的元音才交换

'''


def interchange(str):
    vowels = ['a','e','i','o','u']
    first_position = 0
    second_position = 0
    vowel_num = 0
    for position in range(len(str)):
        if str[position] in vowels:
            vowel_num += 1
            if vowel_num == 3:
                str = "None"
            elif vowel_num == 1:
                first_vowel = str[position]
                first_position = position
            elif vowel_num == 2:
                if str[position] == first_vowel:
                    str = "None"
                else:
                    second_position = position
    if vowel_num == 2:
        str = str[:first_position] + str[second_position] + str[first_position+1:second_position] + str[first_position] + str[second_position+1:]
    else:
        str = "None"
    print(str)


if __name__ == '__main__':
    str = ''
    while str != '0':
        str = input("输入英文字符串(退出输入0)：")
        interchange(str.lower())
    
    