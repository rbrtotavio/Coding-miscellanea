class player:
    def __init__(self, name, race, lvl, life, mana, dmg):
        self.name = name
        self.race = race
        self.lvl = int(lvl)
        self.life = int(life)
        self.totallife = int(life)
        self.mana = int(mana)
        self.totalmana = int(mana)
        self.dmg = int(dmg)

    def revive(self):
        if self.mana >= 50:
            if self.life <= 0:
                life = 0
                life += (self.totallife)/2
                mana -= (50)
                print(self.name +" was resurrected!")
            else:
                print(self.name +" is already alive.")
        else:
            print("Mana is not sufficient!")

    def takedmg(self, dmgtaken):
        self.life -= dmgtaken
        if self.life > 0:
            print(self.name +"'s current life is {}".format(self.life))
        else:
            print(self.name +" is dead.")

    def rest(self):
        if self.mana == self.totalmana:
            print(self.name +"'s mana is full!")
        else:
            self.mana += int(self.totalmana / 2)
            if self.mana >= self.totalmana:
                self.mana -= (self.mana - self.totalmana)
                print(self.name +"'s mana was fully restored!")
            else:
                print(self.name +"'s current mana is {}" .format(self.mana))

teupai = player("Aragorn", "Human", 10, 100, 100, 100)

teupai.takedmg(10)
teupai.revive()
teupai.mana -= 80
teupai.rest()