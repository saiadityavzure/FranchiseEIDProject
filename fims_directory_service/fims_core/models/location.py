from django.db import models
from core.models.base import BaseModel
from .company import Company

class Location(BaseModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="locations"
    )

    class Meta:
        db_table = "locations"
        constraints = [
            models.UniqueConstraint(
                fields=["company", "code"],
                name="uniq_company_location_code"
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"
