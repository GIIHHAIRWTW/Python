file_read = open("D:\B21041022李浩田 Python\文件\README.txt")
file_write = open("D:\B21041022李浩田 Python\文件\README[附件].txt", "w")

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()