import unittest
from client import Client


class TestInitialization(unittest.TestCase):

    def test_throws_an_error_if_no_env(self):
        with self.assertRaises(FileNotFoundError):
            Client()

    def test_checks_if_config_has_all_required_properties(self):
        pass

    def test_scopes_passed_during_initialization(self):
        pass
