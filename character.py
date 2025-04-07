import random

class Character:
    def __init__(self):
        self.__combat_strength = random.randint(1, 6)
        self.__health_points = random.randint(1, 20)
        print(f"{self.__class__.__name__} created with Combat Strength: {self.__combat_strength}, Health Points: {self.__health_points}")

    def __del__(self):
        pass

    # Getter for combat_strength
    @property
    def combat_strength(self):
        return self.__combat_strength

    # Setter for combat_strength
    @combat_strength.setter
    def combat_strength(self, value):
        self.__combat_strength = value

    # Getter for health_points
    @property
    def health_points(self):
        return self.__health_points

    # Setter for health_points
    @health_points.setter
    def health_points(self, value):
        self.__health_points = value
