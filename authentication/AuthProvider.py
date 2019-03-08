from msal import ConfidentialClientApplication

from authentication.ABCAuthentication import ABCAuthentication


class AuthProvider(ABCAuthentication):
    def __init__(self, config):
        self.config = config

    def get_access_token(self):
        app = ConfidentialClientApplication(
            self.config['CLIENT_ID'],
            authority=self.config['AUTHORITY'],
            client_credential=self.config['SECRET']
        )

        result = app.acquire_token_silent(scopes=self.config['scopes'], account=None)

        if not result:
            result = app.acquire_token_for_client(scopes=self.config['scopes'])
        if 'access_token' in result:
            return result['access_token']
