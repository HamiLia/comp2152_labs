from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__() 
        print("The Hero object is being destroyed by the garbage collector")

    def hero_attacks(self, monster):
        print("    |    Hero attacks with strength", self.combat_strength)
        if self.combat_strength >= monster.health_points:
            monster.health_points = 0
            print("    |    You have killed the monster")
        else:
            monster.health_points -= self.combat_strength
            print("    |    You have reduced the monster's health to:", monster.health_points)
