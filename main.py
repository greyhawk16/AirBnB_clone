class Human:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"hello {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


p1 = Player('DDG', 100)
p2 = Fan('SSBN', 'USN')
p2.say_hi()
