from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()
        print("The Monster object is being destroyed by the garbage collector")

    def monster_attacks(self, hero):
        print("    |    Monster attacks with strength", self.combat_strength)
        if self.combat_strength >= hero.health_points:
            hero.health_points = 0
            print("    |    Player is dead")
        else:
            hero.health_points -= self.combat_strength
            print("    |    The monster has reduced Player's health to:", hero.health_points)
