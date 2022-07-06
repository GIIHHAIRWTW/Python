class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))
    def test(self):
        self.__test()


class B(A):
    def demo(self):
        print("%d" % self.__num2)
        self.__test()

b = B()
# print(b.__num2)
b.test() # 子类可以通过调用父类中的调用私有方法的公有方法间接调用私有方法
# b.demo()