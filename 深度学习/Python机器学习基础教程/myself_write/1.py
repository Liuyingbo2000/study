# import matplotlib.pyplot as plt
# from PIL import Image

# # 指定图片路径
# img_path = r"C:\Users\AI CAR\OneDrive\大学课程资料\STUDY\study\深度学习\Python机器学习基础教程\myself_write\a.png"

# # 读取图片
# img = Image.open(img_path)

# # 显示图片
# plt.imshow(img)

# # 隐藏坐标轴
# plt.axis('off')

# # 展示图片
# plt.show()


# import os
# import subprocess

# # 指定文本文件路径
# text_file_path = r"C:\Users\AI CAR\OneDrive\论文\功能介绍.txt"


# # 检查文件是否存在
# if not os.path.isfile(text_file_path):
#     print("File does not exist.")
#     exit()

# # 使用默认文本编辑器打开文件
# subprocess.Popen(['start', 'notepad.exe', text_file_path], shell=True)


# import subprocess

# # 要显示的文本字符串
# text = "Hello, world!"

# # 在新的窗口中显示文本
# subprocess.Popen(['cmd', '/c', 'echo', text])

from tkinter import *

# 创建窗口
root = Tk()

# 设置窗口标题
root.title("新窗口")

# 创建标签控件并添加到窗口中
label = Label(root, text="这是新窗口中的文本")
label.pack()

# 显示窗口
root.mainloop()

