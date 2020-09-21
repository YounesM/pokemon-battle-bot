from models.team import Team


class Game:
    def __init__(self, tag, websocket):
        self.type = ''
        self.tag = ''
        self.team = Team()
        self.enemy_team = Team()
        self.rulesets = []
