class Dog(object):

    #不访问类属性和实例属性
    @staticmethod
    def run():
        print("小狗要跑....")

# 通过类名.调用静态方法----不需要创建对象
Dog.run()