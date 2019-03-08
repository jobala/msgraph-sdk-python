from client import Client
from authentication.AuthProvider import AuthProvider
from config import Config

if __name__ == '__main__':
    config = Config().get_config()

    auth_provider = AuthProvider(config)
    client = Client(auth=auth_provider)
    print(client.get('https://graph.microsoft.com/v1.0/me'))

