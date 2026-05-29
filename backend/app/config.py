"""
Configuration settings for NeuroPath API
"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings"""

    # App settings
    APP_TITLE: str = "NeuroPath"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Infraestructura de Accesibilidad Cognitiva"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Security
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", "your-super-secret-key-change-in-production"
    )
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    )

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/neuropath",
    )
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "neuropath")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")

    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "https://yourdomain.com",
    ]
    CORS_CREDENTIALS: bool = True
    CORS_METHODS: List[str] = ["*"]
    CORS_HEADERS: List[str] = ["*"]

    # LTI Configuration
    LTI_CLIENT_ID: str = os.getenv("LTI_CLIENT_ID", "")
    LTI_CLIENT_SECRET: str = os.getenv("LTI_CLIENT_SECRET", "")
    LTI_ENDPOINT: str = os.getenv("LTI_ENDPOINT", "https://lti-provider.com")

    # Email Configuration
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM: str = os.getenv("SMTP_FROM", "noreply@neuropath.io")

    # AWS S3
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    AWS_BUCKET_NAME: str = os.getenv("AWS_BUCKET_NAME", "neuropath-storage")

    # Sentry
    SENTRY_DSN: str = os.getenv("SENTRY_DSN", "")

    # ML Model Configuration
    ML_MODEL_PATH: str = os.getenv("ML_MODEL_PATH", "/models/lumi_predictor.pkl")
    ML_THRESHOLD_COGNITIVE_FATIGUE: float = float(
        os.getenv("ML_THRESHOLD_COGNITIVE_FATIGUE", "0.75")
    )
    ML_THRESHOLD_ABANDONMENT: float = float(
        os.getenv("ML_THRESHOLD_ABANDONMENT", "0.80")
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
