import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
_USE_SQLITE = os.environ.get("USE_SQLITE", "true").lower() == "true"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = (
    {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB", "gtube"),
            "USER": os.environ.get("POSTGRES_USER", "gtubeadmin"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "gtubedefault"),
            "HOST": os.environ.get("POSTGRES_DB_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }
    if not _USE_SQLITE
    else {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
)
