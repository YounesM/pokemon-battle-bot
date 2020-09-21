import json
from modules.login import login
import modules.logger as logger
from models.game import Game

testing = True
game = None
x = 'global'

async def update_user(websocket, chall):
    if chall != '':
        await login(websocket, chall)


async def set_challenge_id(websocket, message):
    chall = message[0] + '|' + message[1]
    await update_user(websocket, chall)


async def start_game(websocket, message):
    """
    Looks for random battles
    """
    pass


async def accept_challenge(websocket, message):
    if json.loads(message[0])["challengesFrom"]:
        # TODO: Store all current battles in a "Game" Object to handle different requests
        challengers = [k[0] for k in json.loads(message[0])["challengesFrom"].items()]
        logger.log("Accepting challenge: " + challengers[0])
        await websocket.send('|/accept ' + next(iter(challengers)))


async def battle_started(websocket, message):
    game.name = message[2]
    logger.log("Starting battle: " + game.name.strip('\n') + ('(bTag: ' + game.tag + ')'))


async def search_handler(websocket, message):
    global game
    game = Game(websocket)
    if json.loads(message[0])["games"] is not None:
        game.tag = [x[0] for x in json.loads(message[0])["games"].items()][0]

# await websocket.send('|/msg' + message[0] + ', Hey')

async def request_handler(websocket, message):
    if message[0] != '':
        pkm_data = json.loads(message[0])["side"]["pokemon"]
        await game.move(1)


async def receive(websocket, message):
    logger.incoming(message)
    handler = {
        "updateuser": start_game,
        "challstr": set_challenge_id,
        "updatechallenges": accept_challenge,
        "updatesearch": search_handler,
        "init": battle_started,
        "request": request_handler
    }

    if handler.get(message.split('|')[1]) is not None:
        await handler.get(message.split('|')[1])(websocket, message.split('|')[2:])
