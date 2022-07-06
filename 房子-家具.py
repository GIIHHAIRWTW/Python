# 创建家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s 占地%.2f 平米" % (self.name, self.area)

# 创建房子类
class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型:%s\n占地面积:%.2f(剩余%.2f)\n家具:%s"
        % (self.type, self.area, self.free_area, self.item_list))
    def add_item(self,item):
        if item.area > self.area:
            print("%s面积太大，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        print("%s添加成功!" % item.name)
        self.free_area -= item.area

# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("圆桌",1.5)

# 创建房子
my_home = House("四合院", 200)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)



