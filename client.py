from network.Requests import Requests


class Client:
    def __init__(self, auth=None):
        if auth is None:
            raise RuntimeError('AuthProvider missing')
        self.access_token = auth.get_access_token()

    def get(self, path):
        print(self.access_token)
        return Requests().get(path, self.access_token)

