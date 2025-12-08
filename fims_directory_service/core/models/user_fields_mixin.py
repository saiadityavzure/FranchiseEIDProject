from django.db import models
from django.utils import timezone
from datetime import timedelta


def _default_uid_expiry():
    # Approximate 3 months as 90 days to avoid external dependencies.
    return timezone.now() + timedelta(days=90)


class BaseUserFieldsMixin(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    uid_expiry_date = models.DateTimeField(default=_default_uid_expiry)

    class Meta:
        abstract = True
