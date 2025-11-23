from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """
    Shared base model used across the system.
    Includes:
    - created_at / updated_at timestamps
    - status (ENABLED / DISABLED)
    - created_by / last_updated_by audit fields
    """

    STATUS_CHOICES = [
        ("ENABLED", "Enabled"),
        ("DISABLED", "Disabled"),
    ]

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ENABLED",
    )

    created_by = models.CharField(max_length=50, default="system_admin")
    last_updated_by = models.CharField(max_length=50, default="system_admin")

    class Meta:
        abstract = True
