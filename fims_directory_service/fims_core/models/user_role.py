from django.db import models


class UserRole(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    created_by = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)
    last_updated_by = models.CharField(max_length=50, null=True, blank=True)
    last_update_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "user_roles"

    def __str__(self) -> str:
        return self.name
