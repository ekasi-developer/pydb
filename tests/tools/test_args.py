import unittest
from tests import BaseTest
from pydb.tools.args import Args


class ArgsTest(BaseTest):
    def test_throw_exception_parameter_does_not_exist(self):
        with self.assertRaises(Exception):
            Args.guard("name", {})

    def test_return_default_value_parameter_does_not_exist(self):
        default_value = "testing"
        self.assertEqual(Args.guard("database", {}, default_value), default_value)

    def test_return_parameter_value_parameter_exist(self):
        parameters = {"database": "testing_db"}
        self.assertEqual(Args.guard("database", parameters), parameters["database"])


if __name__ == '__main__':
    unittest.main()
