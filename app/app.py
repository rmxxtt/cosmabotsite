import collections

from app.database.database import Database
from app.web.web import Web
from app.bot.bot import Bot
from app.config.parser import read_config


class App:
    def __init__(self):
        self.config = read_config('./config/config.ini')
        self.databse = Database(self.config['database'])
        self.bot = Bot(self.config['bot'])
        self.web = Web(self.config['web'])
        self.command_deque = collections.deque()

    def run(self):
        pass
