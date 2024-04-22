hudud = [
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*"],
]
def print_hudud():
    for i in hudud:
        print(i)


class Anjom:
    kuchi = 10


class Qurol(Anjom):
    def __init__(self, x, y, dushman):
        self.x = x
        self.y = y
        self.dushman = dushman


Bomba = Qurol(3, 3, 20)


class Dori(Anjom):
    def __init__(self, x, y, kuch):
        self.x = x
        self.y = y
        self.kuch = kuch


Aspirin = Dori(2, 2, 15)


class Player:
    def __init__(self, x, y, health, qurollar):
        self.x = x
        self.y = y
        self.health = health
        self.qurollar = qurollar

    def go(self, dx, dy):
        hudud[self.y][self.x] = "*"
        self.x += dx
        self.y += dy
        if self.x == Aspirin.x and self.y == Aspirin.y:
            self.health += Aspirin.kuch
            print(f"Aspirin dorisi qabul qilindi va sog'lik {self.health} bo'ldi!")
        if self.x == Bomba.x and self.y == Bomba.y:
            self.health -= Bomba.dushman
            print(f"Dushman bilan jang qilindi va sog'lik {self.health} bo'ldi!")
        hudud[self.y][self.x] = "P"


Player1 = Player(0, 0, 100, 0)
hudud[Player1.y][Player1.x] = "P"
hudud[Aspirin.y][Aspirin.x] = "D"
hudud[Bomba.y][Bomba.x] = "B"
print_hudud()

while True:
    x = int(input("O'nga yoki chapga yuring: 1 yoki -1, 0: "))
    y = int(input("O'nga yoki chapga yuring: 1 yoki -1, 0: "))
    Player1.go(x, y)
    print_hudud()
