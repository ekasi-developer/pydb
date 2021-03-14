from pydoc import locate
from pydb.tools.args import Args


class Connection(Args):
    def __init__(self, **kwargs):
        self.configurations = {
            "database": self.guard("database", kwargs, ":memory:"),
            "hostname": self.guard("hostname", kwargs, ""),
            "username": self.guard("username", kwargs, ""),
            "password": self.guard("password", kwargs, "")
        }
        self.connection = self.guard("connection", kwargs, "sqlite")

    def connect(self):
        return self.get_connection_class(self.configurations)

    @property
    def get_connection_class(self):
        return locate(f"pydb.connection.{self.connection}.{str(self.connection).capitalize()}")
