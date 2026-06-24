from dataclasses import dataclass 

@dataclass(frozen=True)
class Settings:    
    data_base_url: str 
    cors_allow_origins: list[str]


def get_settings() -> Settings: 
    return Settings(
        data_base_url="postgresql+psycopg2://postgres:admin@127.0.0.1:5432/postgres", 
        cors_allow_origins=["*"],
    )

