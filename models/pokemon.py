import requests
import asyncio


class Pokemon:
    def __init__(self, name, level):
        """
        :param name: The pokemon's name
        :param level: The pokemon's level
        """
        self.name = name
        self.level = level
        self.status = None
        self.types = []
        self.base_stats = {"atk": 0, "spa": 0, "def": 0, "spd": 0, "spe": 0}
        self.moves = []
        self.boons = {"atk": 0, "spa": 0, "def": 0, "spd": 0, "spe": 0, "eva": 0, "acc": 0}
        self.item = ''
        self.abilities = []

        self.load(name)

    @classmethod
    async def load(cls, name):
        pass
