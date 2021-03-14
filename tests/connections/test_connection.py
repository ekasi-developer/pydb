import unittest, random, math, os
from tests import BaseTest
from pydb.connection.sqlite import Sqlite
from pydb.connection import Connection


class ConnectionsTest(BaseTest):
    def setUp(self) -> None:
        random.seed(random.randint(100, 1000))

    def test_connect_to_database_with_default_settings(self):
        conn = Connection()
        self.assertIsInstance(conn.connect(), Sqlite)

    def test_create_connection_custom_settings(self):
        db = self.temp_path(f"database-{math.floor(random.random()*10000)}.db")
        Connection(database=db).connect()
        self.assertTrue(os.path.exists(db))
        os.remove(db)  # delete file in temp path


if __name__ == '__main__':
    unittest.main()
