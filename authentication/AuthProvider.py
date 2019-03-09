from msal import PublicClientApplication

from authentication.ABCAuthentication import ABCAuthentication


class AuthProvider(ABCAuthentication):
    def __init__(self, config):
        self.config = config

    def get_access_token(self):
        result = None

        app = PublicClientApplication(
            self.config['CLIENT_ID'],
            authority=self.config['AUTHORITY'],
        )

        accounts = app.get_accounts()

        if accounts:
            chosen_account = accounts[0]
            result = app.acquire_token_silent(self.config['scopes'], account=chosen_account)

        if not result:
            result = app.acquire_token_by_username_password(
                self.config['USERNAME'],
                self.config['SECRET'],
                scopes=self.config['scopes']
            )

            print(result)
        return result['access_token']
