from django.db import models
from django.contrib.auth.models import AbstractUser as _User, UserManager
import uuid
from src.preferences.schemas import DTYPE


class UserPreference(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    preference = models.ForeignKey("preferences.Preference", on_delete=models.CASCADE)
    raw_value: str | models.TextField = models.TextField()

    @property
    def value(self):
        import json

        if self.preference.type == DTYPE.STRING.value:
            return self.raw_value
        elif self.preference.type == DTYPE.BOOL.value:
            return self.raw_value.lower() == "true"
        elif self.preference.type == DTYPE.INT.value:
            return int(self.raw_value)
        elif self.preference.type == DTYPE.FLOAT.value:
            return float(self.raw_value)
        elif self.preference.type == DTYPE.STRING.value:
            return self.raw_value
        elif self.preference.type == DTYPE.JSON.value:
            return json.loads(self.raw_value)
        else:
            raise ValueError(f"Unknown type {self.preference.type}")

    @value.setter
    def value_setter(self, value: str | int | float | bool | dict | list):
        import json

        if self.preference.type == DTYPE.STRING.value:
            assert isinstance(value, str)
            self.raw_value = value
        elif self.preference.type == DTYPE.BOOL.value:
            assert isinstance(value, bool)
            self.raw_value = value
        elif self.preference.type == DTYPE.INT.value:
            assert isinstance(value, int)
            self.raw_value = str(int(value))
        elif self.preference.type == DTYPE.FLOAT.value:
            assert isinstance(value, float)
            self.raw_value = str(float(value))
        elif self.preference.type == DTYPE.JSON.value:
            assert isinstance(value, dict) or isinstance(value, list)
            self.raw_value = json.dumps(value)


class User(_User):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    preferences = models.ManyToManyField(
        "preferences.Preference",
        through="UserPreference",
        related_name="users",
    )

    objects = UserManager()
