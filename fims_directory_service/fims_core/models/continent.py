from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = "continents"
        ordering = ["id"] 

    def __str__(self) -> str:
        return self.name
