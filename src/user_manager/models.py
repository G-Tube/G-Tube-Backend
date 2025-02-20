import uuid

from django.contrib.auth.models import AbstractUser as _User
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.preferences.schemas import DTYPE


class UserPreference(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    preference = models.ForeignKey("preferences.Preference", on_delete=models.CASCADE)
    raw_value: str | models.TextField = models.TextField()

    class Meta:
        unique_together = ("user", "preference")

    @property
    def value(self):
        import json

        if self.preference.dtype == DTYPE.STRING.value:
            return self.raw_value
        elif self.preference.dtype == DTYPE.BOOL.value:
            return self.raw_value.lower() == "true"
        elif self.preference.dtype == DTYPE.INT.value:
            return int(self.raw_value)
        elif self.preference.dtype == DTYPE.FLOAT.value:
            return float(self.raw_value)
        elif self.preference.dtype == DTYPE.STRING.value:
            return self.raw_value
        elif self.preference.dtype == DTYPE.JSON.value:
            return json.loads(self.raw_value)
        else:
            raise ValueError(f"Unknown type {self.preference.type}")

    @value.setter
    def value_setter(self, value: str | int | float | bool | dict | list):
        import json

        if self.preference.dtype == DTYPE.STRING.value:
            assert isinstance(value, str)
            self.raw_value = value
        elif self.preference.dtype == DTYPE.BOOL.value:
            assert isinstance(value, bool)
            self.raw_value = value
        elif self.preference.dtype == DTYPE.INT.value:
            assert isinstance(value, int)
            self.raw_value = str(int(value))
        elif self.preference.dtype == DTYPE.FLOAT.value:
            assert isinstance(value, float)
            self.raw_value = str(float(value))
        elif self.preference.dtype == DTYPE.JSON.value:
            assert isinstance(value, dict) or isinstance(value, list)
            self.raw_value = json.dumps(value)


class User(_User):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    preferences = models.ManyToManyField(
        "preferences.Preference",
        through="UserPreference",
        related_name="users",
    )
    email = models.EmailField(_("email address"), unique=True)
    dp = models.ImageField(
        upload_to="profile_pics",
        default="../static/default-dp.jpg",
    )
    cover = models.ImageField(
        upload_to="cover_pics",
        default="../static/default-cover.jpg",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
