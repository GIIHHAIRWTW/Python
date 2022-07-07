class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        # 返回对象的引用
        return super().__new__(cls)
    
    def __init__(self):
        print("播放器初始化....")

player = MusicPlayer()
print(player)