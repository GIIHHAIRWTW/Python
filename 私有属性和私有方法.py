class Women:
    def __init__(self, name):
        self.name = name
        # 私有属性，
        self.__age = 18
    # 私有方法    
    def __secret(self):
        print("%s的年龄是%d岁" % (self.name, self.__age))
XiaoFang = Women("小芳")

# 访问私有属性和私有方法的方法   _类名__属性/方法
print(XiaoFang._Women__age)
XiaoFang._Women__secret()
