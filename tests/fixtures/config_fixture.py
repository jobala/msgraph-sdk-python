from pathlib import Path
import os

env_path = Path.joinpath(Path.cwd().parent, '.env')


def create_env_with_all_properties():
    env_path.write_text(
        'AUTHORITY=authority\nCLIENT_ID=client_id\nSECRET=secret\n'
    )


def create_env_with_missing_property():
    env_path.write_text('AUTHORITY=authority\n')
    env_path.write_text('CLIENT_ID=client_id\n')


def remove_env_file():
    os.remove(env_path)
