import unittest
from tests import BaseTest
from pydb.connection import Connection


class SqliteQueryTest(BaseTest):
    def setUp(self) -> None:
        self.connection = Connection()

    def test_execute_sql_statement(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
