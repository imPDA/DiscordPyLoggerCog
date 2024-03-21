import pathlib

import environ
from pydantic import BaseModel

BASE_FOLDER = pathlib.Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(BASE_FOLDER / ".env")


class Settings(BaseModel):
    discord_token: str = env('DISCORD_TOKEN')
    logging_channel_id: int = env('LOGGING_CHANNEL_ID', cast=int)
    test_server_id: int = env('TEST_SERVER_ID', cast=int)


bot_settings = Settings()
