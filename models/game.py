from models.team import Team
import asyncio


class Game:
    def __init__(self, websocket):
        self.name = ''
        self.type = ''
        self.tag = ''
        self.team = Team()
        self.enemy_team = Team()
        self.rulesets = []
        self.websocket = websocket

        self.weather = ''
        self.terrain = ''
        self.screens = []
        self.gravity = False
        self.can_switch = True
        self.trick_room = False
        self.traps = []

    async def move(self, number):
        # TODO: action to use a move
        # await self.websocket.send('|/query roomlist')
        await self.websocket.send('|' + self.tag + '|/mv ' + str(number))
        pass

    def switch(self, number):
        # TODO: switch to another pkm
        pass

    def activate_gimmic(self):
        # TODO: activate gimmic (ex: Dynamax)
        pass
