from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    base_url: str = "https://saucedemo.com"
    screenshots_dir: str = "reports/screenshots"

SETTINGS = Settings()