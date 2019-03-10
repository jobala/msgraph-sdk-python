import unittest

from tests.fixtures.fixture_auth import FixtureAuth
from client import Client


class TestAuth(unittest.TestCase):
    def test_gets_token(self):
        auth_provider = FixtureAuth()
        client = Client(auth=auth_provider)

        self.assertEqual(client.access_token, 'A token')
