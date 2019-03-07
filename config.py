from pathlib import Path
from dotenv import load_dotenv
import os


class Config:
    def __init__(self, scopes=['https://graph.microsoft.com/.default']):
        self.required_env_vars = ['AUTHORITY', 'SECRET', 'CLIENT_ID']
        self.config = {}
        self.load_config()

        self.config.update({'scopes': scopes})

    def get_config(self):
        return self.config

    def load_config(self):
        env_path = Path.joinpath(Path.cwd(), '.env')
        env_file = Path(env_path)

        try:
            env_file.resolve(strict=True)
        except FileNotFoundError:
            raise FileNotFoundError('.env file does not exist.')
        else:
            self.check_env_vars(env_file)
            load_dotenv(dotenv_path=env_file)
            self.hydrate_config()

    def check_env_vars(self, env_file):
        env_vars = env_file.read_text()
        for env_var in self.required_env_vars:
            if env_vars.rfind(env_var) == -1:
                raise RuntimeError('Key missing {}'.format(env_var))

    def hydrate_config(self):
        for env_var in self.required_env_vars:
            self.config.update({env_var: os.getenv(env_var)})

