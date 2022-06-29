str1 = "Hello World!"
for c in str1:
    print(c)
print(str1[4])

# 统计字符串长度
print(len(str1))

# 统计小字符串出现的次数
print(str1.count("lo"))

# 小字符串出现的位置
print(str1.index("lo"))

# 判断类型-9
'''
str1.isspace()    字符串中只有空格，则返回True
str1.isalnum()    至少有一个字符并且所有字符都是字母或数字，则返回True
str1.isalpha()    至少有一个字符并且所有字符都是字母，则返回True
str1.isdecimal()  只包含数字则返回True，全角数字
str1.isdigit()       只包含数字则返回True，全角数字、(1)、\u00b2
str1.isnumeric()  只包含数字则返回True，全角数字、汉字数字
str1.istitle()        标题化的(每个单词首字母大写)则返回True
str1.islower()      包含至少一个区分大小写的字符，并且这些(区分大小写的)字符都是小写，则返回True
str1.isupper()    包含至少一个区分大小写的字符，并且这些(区分大小写的)字符都是大写，则返回True
'''

space_str = " \t\r\n "
print(space_str.isspace())

num_str = "123"
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 查找和替换-7
"""
str.startswith(str)  检查字符串是否以str开头，是返回True
str.endswith(str)    检查字符串是否以str结尾，是返回True
str.find(str,start=(),end=len(str))  检查str是否包含在字符串中，start和end指定范围，在指定范围返回开始索引，否则返回-1
str.rfind(str,start=(),end=len(str)) 类似于find()函数，从右边开始查找
str.index(str,start=(),end=len(str)) 跟find()函数类似，str不在字符串中会报错
str.rindex(str,start=(),end=len(str)) 类似于index()函数，从右边开始查找
str.replace(old_str,new_str,num=str.count(old)) 把str中的old_str替换成new_str,如果num指定，则替换不超过num次，返回一个新字符串
"""

hello_str = "hello world"
print(hello_str.startswith("hello"))
print(hello_str.endswith("world"))
print(hello_str.find("llo"))
print(hello_str.replace("world", "python"))
print(hello_str)

# 文本对齐-3
'''
str.ljust(width)      返回一个原字符串左对齐，并使用空格填充至长度width的新字符串
str.rjust(width)     返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
str.center(width)  返回一个原字符串居中对齐，并使用空格填充至长度width的新字符串
'''

poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(10))

# 去除空白字符-3
'''
str.lstrip()    截掉str左边(开始)的空白字符
str.rstrip()    截掉str右边(开始)的空白字符
str.strip()      截掉str左右两边的空白字符
'''

poem1 = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽",
         "黄河入海流\t\n",
         "欲穷千里目",
         "更上一层楼"]

for poem1_str in poem:
    print("|%s|" % poem1_str.center(10))

# 拆分和连接-5
'''
string.partition(str)   把字符串string分成一个3元素的元组(str前面，str，str后面)
string.rpartition(str)  类似于partition()，不过从右边开始
string.split(str="",num)    以str为分隔符拆分string，若num有指定值，则仅分隔num+1个子字符串，str默认包含'\t','\n','\r'和空格
string.splitlines()        按照行('\r','\n','\r\n')分隔，返回一个包含各行作为元素的列表
string.join(seq)        以string作为分隔符，将seq中所有元素(的字符串表示)合并为一个新的字符串
'''

