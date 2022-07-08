try:
    num = int(input("请输入一个整数:"))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print("分母不能为0!")

except ValueError:
    print("请输入正确的整数!")

except Exception as result:
    print("未知错误! %s" % result)

else:
    # 没有异常执行的代码
    print("hehe")

finally:
    # 无论有无异常都会执行的代码
    print("haha")