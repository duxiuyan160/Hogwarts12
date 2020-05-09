"""
  一个回合制游戏，每个角色都有hp和power,
  hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为1000，power的初始值为200.
  定义一个fight方法：
  final_hp = hp-enemy_power
  enemy_final_hp = enemy_hp-power
  两个hp进行对比，血量剩余多的人获胜
  """
class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def fight(self,enemy_power,enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

"""
第二个角色，他叫后裔，后裔继承了角色的hp和power。并多了护甲属性。
houyi_hp = hp + defense - enemy_power
"""
class Houyi(Game):
    def __init__(self):
        super().__init__(1000,200)         #如果在子类中重新定义了__init__,那么父类的__init__将会被覆盖
        self.defense = 100
    def houyi_fight(self,enemy_power,enemy_hp):
        final_hp = self.hp +self.defense- enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

def test_game():
    hp = 1000
    power = 200
    # game = Game(hp,power)
    # game.fight(2100,200)
    houyi = Houyi()
    houyi.houyi_fight(hp,power)