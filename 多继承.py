# 如果父类之间存在同名的属性或方法，应该尽量避免使用多继承
# object是所有类的父类，也叫基类，创建类时python3默认继承object，python2则需手动继承
class A(object):
    def test(self):
        print("test方法")

class B(object):
    def demo(self):
        print("demo方法")

class C(A, B):
    pass

c = C()
c.test()
c.demo()
# dir() 查看类中的所有方法
print(dir(c))