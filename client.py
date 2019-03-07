class Client:
    def __init__(self, auth=None):
        if auth is None:
            raise RuntimeError('AuthProvider missing')
        self.access_token = auth.get_access_token()

