from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    base_url: str = "https://demo.nopcommerce.com"
    screenshots_dir: str = "reports/screenshots"

settings = Settings()