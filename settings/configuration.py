
"""
This configuration file is used to set up the application configuration

"""
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Config(BaseSettings):
    
    db_url: str
    bot_api_key: str

    class Config:
        """
        Configuration settings for the application
        """
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()

if __name__ == "__main__":
    print(config.db_url, "\n"+config.bot_api_key)