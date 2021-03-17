import unittest
from tests import BaseTest
from pydb.query.sql.statement import Statement


class SqlStatementTest(BaseTest):
    def test_create_sql_statement(self):
        sql_statement = Statement()
        self.assertIsInstance(sql_statement, Statement)


if __name__ == "main":
    unittest.main()
