import random

n = random.randint(1, 100)
a = 0
while 1:
    number = int(input("请输入一个1-100之间的整数: "))
    a = a + 1
    if n > number:
        print("你猜的小了！")
    elif n < number:
        print("你猜的大了！")
    else:
        print("Congratulation!")
        break
print("游戏结束！")
print("您猜了 %d 次。" % a)
