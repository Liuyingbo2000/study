# 3.2天天向上的力量

# 1%的力量

# dayup = pow(1.001, 365)
# daydown = pow(0.999, 365)
# print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))


# 5%0和1%的力量

# dayfactor = 0.005
# dayup = pow(1+dayfactor, 365)
# daydown  = pow(1-dayfactor, 365)
# print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

# 工作日的力量

# dayup = 1.0
# dayfactor = 0.01
# for i in range(365):
#     if i % 7 in [6, 0]:
#         dayup = dayup*(1-dayfactor)
#     else:
#         dayup = dayup*(1+dayfactor)
# print("工作日的力量:{:.2f}".format(dayup))

# 工作日的努力

# def dayUP(df):
#     dayup = 1.0
#     for i in range(365):
#         if i % 7 in [6, 0]:
#             dayup = dayup*(1-0.001)
#         else:
#             dayup = dayup*(1+df)
#     return dayup
# dayfactor = 0.01
# while dayUP(dayfactor) < 37.78:
#     dayfactor += 0.001
# print("工作日的努力参数是:{:.3f}".format(dayfactor))


# 获取星期字符串
weekStr = "一二三四五六七"
weekId = eval(input("请输入星期的数字(1-7):"))
print("星期" + weekStr[weekId-1])