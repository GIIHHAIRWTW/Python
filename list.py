name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[2])

# 确定下标
print(name_list.index("wangwu"))

# 修改
name_list[1] = "李四"

# 增加
name_list.append("王小二")
name_list.insert(1, "张小三")

temp_list = ["孙悟空", "猪八戒", "沙和尚"]
name_list.extend(temp_list)

# 删除
print(name_list)
name_list.remove("wangwu")
# pop默认删除最后一个元素
name_list.pop()
name_list.pop(3)

# 把变量从内存中删除，删除后，后续不能使用
del name_list[1]

# name_list.clear()

print(name_list)

# 列表长度 and 元素出现次数
list_len = len(name_list)
print("%d个元素" % list_len)

count = name_list.count("zhangsan")
print("\"zhangsan\"出现%d次" % count)


# 升序 and 降序
# name_list.sort()
# name_list.sort(reverse=True)

# 逆序
name_list.reverse()
print(name_list)
