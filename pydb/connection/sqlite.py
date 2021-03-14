import sqlite3
from pydb.tools.args import Args


class Sqlite:
    def __init__(self, config):
        self.db = sqlite3.connect(config["database"])

    def connect(self):
        return self.db.cursor()

    def disconnect(self) -> None:
        self.db.close()
