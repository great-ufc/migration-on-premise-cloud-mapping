from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    API_HOST: str = "localhost"
    API_PORT: int = 8000

    CHROMA_PATH: str = "chroma"
    DATA_PATH: str = "data"
    
    OLLAMA_BASE_URL: str = "http://llm:11434"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

settings = Config()
