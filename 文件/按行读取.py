file = open("D:\B21041022李浩田 Python\文件\README.txt", encoding = "UTF-8")

while True:
    text = file.readline()
    if not text:
        break
    print(text, end="")

file.close()