name_list = ["张三", "李四", "王五", "王小二"]

# 顺序地从列表中获取数据
for my_name in name_list:
    print("我的名字叫%s" % my_name)


# 元组（元素不能修改）
info_tuple = ("zhangsan", 18, 175)
empty_tuple = ()   # 空元组
single_tuple = (5,)   # 只有一个元素的元组

print(info_tuple[0])
print(info_tuple.index("zhangsan"))
print(info_tuple.count("zhangsan"))
print(len(info_tuple))

for my_info in info_tuple:
    print(my_info)


info = ("张三", 18)
print("%s年龄是%d" % info)

# 元组和列表类型转换
list()
tuple()


# 字典(无序的对象集合)
xiaoming = {"name": "小明",
                     "age": 18,
                     "gender": True,
                     "height": 175}
# 取值
print(xiaoming["name"])

# 增加 and 修改
xiaoming["weight"] = 60
xiaoming["name"] = "xiaoming"
print(xiaoming)

# 删除
xiaoming.pop("weight")
print(xiaoming)

# 统计键值对数量
print(len(xiaoming))

# 合并字典(相同键，值替换)
temp_dict = {"grade": 600}
xiaoming.update(temp_dict)
print(xiaoming)

# 清空字典
xiaoming.clear()
print(xiaoming)

# 遍历字典
xiaoming = {"name": "小明",
                     "age": 18,
                     "gender": True,
                     "height": 175}
for k in xiaoming:
    print("%s:%s" % (k, xiaoming[k]))


# 多个字典放在一个列表中
card_list = [{"name": "张三",
              "qq": "123456",
              "phone": "110"},
             {"name": "李四",
              "qq": "654321",
              "phone": "119"}]
for card_info in card_list:
    print(card_info)
