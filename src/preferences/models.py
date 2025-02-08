from django.db import models
from src.common.models import BaseModel
from src.preferences.schemas import DTYPE


class Preference(BaseModel):
    key = models.CharField(max_length=30, primary_key=True)
    dtype = models.IntegerField(choices=DTYPE.choices(), default=0)
    description = models.TextField(blank=True, null=True)
