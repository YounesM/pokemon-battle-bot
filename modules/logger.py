import datetime


def display_date():
    print("[{}]".format(datetime.datetime.now().replace(microsecond=0).isoformat()), end='')


def incoming(message):
    display_date()
    print("({}) \t{}".format(message.split('|')[1], message.split('|')[2:]))


def log(message):
    display_date()
    print('[>> LOG] \t' + message)
