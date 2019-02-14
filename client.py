from pathlib import Path
from dotenv import load_dotenv


class Client:
    def __init__(self, scopes=[]):
        # TODO: Understand kwargs
        self.config = {}
        self.load_config()

    def load_config(self):
        # TODO: Understand how property access works in python
        env_file = Path('/.env')

        try:
            env_file.resolve(strict=True)
        except FileNotFoundError:
            raise FileNotFoundError('.env file does not exist.')
        else:
            load_dotenv()
