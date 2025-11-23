from django.db import models
from .continent import Continent


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True)

    continent = models.ForeignKey(
        Continent,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="countries",
    )

    class Meta:
        db_table = "countries"

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"
