class Pet:
    def __init__(
        self,
        name="noname",
        fullness=0,
        health=0,
        mood=0,
        cleanness=0,
        energy=0,
    ):
        self.portrait = ""
        self.name = name
        self.fullness = fullness
        self.health = health
        self.mood = mood 
        self.cleanness = cleanness
        self.energy = energy
        self.fullness_change = -1
        self.health_change = -1
        self.mood_change = -1 
        self.cleanness_change = -1
        self.energy_change = -1 

    def feed(self, num):
        self.fullness += num
        print(f"{self.name} съел {num} и у него {slef.fullness}")

    """
        рисовать питомца
        способности питомца
        показатели питомца
        время
    """
