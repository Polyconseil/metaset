import os

import django
from django.conf import settings


def pytest_configure():
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "metaset_test",
                "HOST": os.getenv("DB_HOST", ""),
                "PORT": int(os.getenv("DB_PORT", 5432)),
                "USER": os.getenv("DB_USER", ""),
                "PASSWORD": os.getenv("DB_PASSWORD", ""),
            }
        },
        INSTALLED_APPS=["tests.django_test_app"],
    )
    django.setup()
