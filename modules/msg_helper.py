import json
from modules.login import login
import modules.logger as logger

testing = True


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
        logger.log("Accepting challenge: " + json.loads(message[0])["challengesFrom"])
        websocket.send('|/accept ' + next(iter(json.loads(message[0])["challengesFrom"])))


# await websocket.send('|/msg' + message[0] + ', Hey')


async def receive(websocket, message):
    logger.incoming(message)
    handler = {
        "updateuser": start_game,
        "challstr": set_challenge_id,
        "updatechallenges": accept_challenge
    }

    if handler.get(message.split('|')[1]) is not None:
        await handler.get(message.split('|')[1])(websocket, message.split('|')[2:])
