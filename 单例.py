class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        print("初始化")
        # 修改类属性标记
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)