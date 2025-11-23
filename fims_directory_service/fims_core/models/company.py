from django.db import models
from core.models.base import BaseModel
from .country import Country

class Company(BaseModel):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    comp_code = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return f"{self.name} ({self.comp_code})"
