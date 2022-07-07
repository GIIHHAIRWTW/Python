class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name
    
    @staticmethod
    def show_help():
        print("帮助信息:让僵尸进门")
    
    @classmethod
    def show_top_score(cls):
        print("历史最高分:%d" % cls.top_score)
    
    def start_game(self):
        print("%s 开始游戏了...." % self.player_name)

# 查看游戏帮助
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建玩家，开始游戏
game = Game("小明")
game.start_game()
