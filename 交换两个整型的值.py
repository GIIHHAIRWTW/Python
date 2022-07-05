a = 3
b = 5

# 1.创建临时变量
# c = a
# a = b
# b = c

# 2.不创建临时变量
# a = a + b
# b = a - b
# a = a - b

# a = a^b
# b = a^b
# a = a^b

# 3.Python特有解法
a, b =(b, a)
print(a, b)
