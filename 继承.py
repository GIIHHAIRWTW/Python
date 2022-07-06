# 继承具有传递性
class Animal:
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")
    def run(self):
        print("run")
    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("汪汪汪....")


class FlyDog(Dog):
    def fly(self):
        print("fly")
    # 重写父类bark方法
    def bark(self):
        print("嗷呜....")

        # python 2.0 用  父类名.方法(self)   调用父类方法
        Dog.bark(self)

    # 扩展父类bark方法
    def bark(self):
        print("嗷呜....")
        return super().bark()


wangcai = FlyDog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()
