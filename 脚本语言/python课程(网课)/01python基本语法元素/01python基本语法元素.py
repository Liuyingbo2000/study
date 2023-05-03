"""
# 第一章python基本语法元素
##   1.1程序设计方法
##   1.2python开发环境配置
##   1.3实列1：温度转换
##   1.4python语法元素分析
"""
"""
##      1.1程序设计方法
"""
# 编译，解释；源代码和目标代码
# 编译（一次性翻译），解释（每次翻译）。
# 静态语言 —— 使用编译执行的编程程序C/C++、Java语言
# 脚本语言 —— 使用解释执行的编程语言Python、JavaScrip语言、PHP语言

# 程序编写方法 —— IPO   I（input) O(output) P(process)
# 编程解决问题步骤
#   分析问题，规划IPO，关注算法，编写程序，调试，完善代码。

"""
##      1.2Python开发环境配置
"""
# Python的两种编程方式
# 交互式，文件式

# 圆面积
# r = 25
# area = 3.1415 * r * r
# print(area)
# print("{:.2f}".format(area))

# 同切圆绘制
# import turtle
# turtle.pensize(2)
# turtle.circle(10)
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)

# 五角星
# from turtle import *
# color('red','red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()
# down()

# 1.3温度转换实列
TempStr = input("请输入带有符号的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
    
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("格式错误")

# 1.4python语法元素分析
'''
代码高亮
缩进,多层缩进
注释
命名与保留字,变量,(大小写敏感),python 33个保留字
数据类型:字符串,整数,列表,浮点数.
'''

'''
分支语句
函数
eval()评估函数,括号中的引号去掉
{:.2f}槽
.format(c)
'''

# 练习
