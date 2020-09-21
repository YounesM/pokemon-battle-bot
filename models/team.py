from models.pokemon import Pokemon


class Team:
    def __init__(self):
        self.pkms = []
        self.active = 0

    def add(self, pkmlist):
        rawpkms = pkmlist
        for pkm in rawpkms:
            self.pkms.append(Pokemon(pkm.split('|')[0], pkm.split('|')[1]))

    def switch(self, number):
        self.active = number
