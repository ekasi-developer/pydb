import unittest
from tests import BaseTest
from pydb.connection.sqlite import Sqlite


class SqliteConnectionTest(BaseTest):
    def setUp(self) -> None:
        self.sqlite_db = Sqlite({'database': ":memory:"})

    def test_connect_database(self):
        self.assertIsNotNone(self.sqlite_db.connect())

    def test_disconnect_database(self):
        self.sqlite_db.connect()
        self.sqlite_db.disconnect()
        with self.assertRaises(Exception):
            self.sqlite_db.db.execute("CREATE TABLE people(fullname TEXT)")


if __name__ == '__main__':
    unittest.main()
