from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str

    @property
    def URL(self):
        return f'postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}'
    
    class Config:
        env_file = '.env'


cnf = Settings()
