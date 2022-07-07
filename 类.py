class human:
    def age(self):
        age = 18;
        print("%s" % self.name)
        print("age = %d" % age)
    def height(self):
        height = 175;
        print("height = %d" % height)
    def weight(self):
        weight = 110;
        print("weight = %d" % weight)
a = human()
a.name = "小明"
a.age()
a.height()
a.weight()

class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了" % self.name)
    def __del__ (self):
        print("%s 走了" % self.name)
tom = Cat("TOM")
print("-" * 50)