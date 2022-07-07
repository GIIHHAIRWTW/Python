# 不同的子类对象调用相同的方法产生不同的结果
class Dog(object):
    def __init__(self, name):
        self.name = name
    def play(self):
        print("%s 在地上蹦蹦跳跳...." % self.name)


class FlyDog(Dog):
    def play(self):
        print("%s 在天上飞来飞去...." % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name
    def play_with_dog(self, dog):
        print("%s 和 %s快乐地玩耍...." % (self.name, dog.name))
        dog.play()

wangcai = FlyDog("旺财")
xiaoming = Person("小明")
xiaoming.play_with_dog(wangcai)
