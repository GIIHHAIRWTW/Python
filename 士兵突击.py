class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_num = 0
    def add_bullet(self, num):
        self.bullet_num += num
    def shoot(self):
        if self.bullet_num <= 0:
            print("%s 没有子弹了...." % self.model)
            return
        self.bullet_num -= 1
        print("%s biu biu biu.... %s" % (self.model, self.bullet_num))


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return
        print("冲啊!!! %s" % self.name)
        # self.gun.add_bullet(50)
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")

# 创建士兵许三多
许三多 = Soldier("许三多")
许三多.gun = ak47
许三多.gun.add_bullet(50)
许三多.fire()