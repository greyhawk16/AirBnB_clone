class Player:
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def say_hi(self):
        return f'hello, {self.name}'


p1 = Player('DDG', 16)
print(p1.say_hi())
