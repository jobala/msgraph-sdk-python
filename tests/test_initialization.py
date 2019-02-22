import unittest

from client import Client
from tests.fixtures.config_fixture import\
    create_env_with_missing_property,\
    create_env_with_all_properties,\
    remove_env_file


class TestInitialization(unittest.TestCase):

    def test_raise_an_error_if_no_env(self):
        with self.assertRaises(FileNotFoundError):
            Client()

    def test_checks_if_config_has_all_required_properties(self):
        create_env_with_missing_property()
        with self.assertRaises(TypeError):
            Client()
        remove_env_file()

    def test_scopes_passed_during_initialization(self):
        create_env_with_all_properties()

        client = Client()
        scopes = client.config.get('scopes', None)
        self.assertEqual(scopes, 'https://graph.microsoft.com/.default')

        client = Client(['User.ReadWrite'])
        scopes = client.config.get('scopes', None)
        self.assertEqual(scopes, ['User.ReadWrite'])

