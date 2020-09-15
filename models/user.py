class User:
    def __init__(self, values):
        self.username = values[0].trim()
        self.challstr = ''
        self.isLogged = False

