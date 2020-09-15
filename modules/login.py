import requests
import json
import sys
import modules.logger as logger

async def login(websocket, challstr):
    with open(sys.path[0] + '/login', 'r') as login_file:
        username = login_file.readline()[:-1]
        password = login_file.readline()[:-1]
        resp = requests.post('https://play.pokemonshowdown.com/action.php?', data={'act': 'login',
                                                                                   'name': username,
                                                                                   'pass': password,
                                                                                   'challstr': challstr})
        logger.log(resp.text[1:])

        await websocket.send('|/trn '+username+',0,'+json.loads(resp.text[1:])["assertion"])
