import unittest

from config import Config
from tests.fixtures.config_fixture import\
    create_env_with_missing_property,\
    create_env_with_all_properties,\
    remove_env_file


class TestConfig(unittest.TestCase):

    def test_raise_an_error_if_no_env(self):
        with self.assertRaises(FileNotFoundError):
            Config()

    def test_checks_if_config_has_all_required_properties(self):
        create_env_with_missing_property()
        with self.assertRaises(TypeError):
            Config()
        remove_env_file()

    def test_scopes_passed_during_initialization(self):
        create_env_with_all_properties()

        config = Config()
        scopes = config.config.get('scopes', None)
        self.assertEqual(scopes, ['https://graph.microsoft.com/.default'])

        config = Config(['User.ReadWrite'])
        scopes = config.config.get('scopes', None)
        self.assertEqual(scopes, ['User.ReadWrite'])

