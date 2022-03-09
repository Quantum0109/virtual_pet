class Pet:
    """
       живой ли питомец 
       сытость:
       ограничение
       при кормлении +5
       когда спит -0.5
       менять портрет когда ест
       если не здоров то либо не ест либо тошнит
       настроение:
       при игре сытость - 5 энергия - 5 но пасторение + 10
       чистота - 10
       если не здоров не играет
       сон:
       спит пока не разбудят либо пока энергия = 100
       здоровье +1 в тик
       зависит от еды и энергии
       если здоровье = 0 то смерть
       елси настроение меньше 15 то картика sad

       всё меняется постепенно
       занятость 

    """
    def __init__(
        self,
        name="неизветно",
        fullness=0,
        health=0,
        mood=0,
        cleanness=0,
        energy=0
    ):
        self.portrait = "assets/calm.png"
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
        print(f"{self.name} съел {num} и теперь у него {self.fullness} сытости")

    def change_portrait(self):
        pass

    def decrease_stats(self):
            self.fullness += self.fullness_change
            self.health += self.health_change
            self.mood += self.mood_change
            self.cleanness += self.cleanness_change
            self.energy += self.energy_change