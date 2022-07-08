# vscode中因为终端默认路径的问题，打开文件要使用绝对路径   ' encoding = "UTF-8"解决中文乱码问题 '
file = open("D:\B21041022李浩田 Python\文件\README.txt",encoding = "UTF-8")

text = file.read()
print(text)

file.close()