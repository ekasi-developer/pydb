import os
from unittest import TestCase

BASE_PATH = os.path.abspath(__file__).replace(os.path.basename(__file__), "")


class BaseTest(TestCase):
    @staticmethod
    def temp_path(filename):
        return f"{BASE_PATH}/temp/{filename}"
