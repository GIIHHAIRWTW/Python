class Tool(object):
    count = 0

    # 定义一个类方法
    @classmethod
    def show_tool_num(cls):
        print("工具对象的数量是 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("扳手")
Tool.show_tool_num()