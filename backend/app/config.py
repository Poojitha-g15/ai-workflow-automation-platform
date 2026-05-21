from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Workflow Automation Platform"
    environment: str = "local"
    database_url: str = "sqlite:///./workflow.db"
    local_fallback_mode: bool = True
    ai_provider: str = "fallback"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
