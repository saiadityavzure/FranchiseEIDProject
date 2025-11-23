from django.db import models
from django.utils import timezone


class IdentityRegistry(models.Model):
    class EmployeeType(models.TextChoices):
        CORP_ADMIN = "corp_admin", "Corporate Admin"
        LOC_ADMIN = "loc_admin", "Location Admin"
        LOCATION_USER = "location_user", "Location User"

    eid = models.CharField(max_length=50, unique=True)

    # which kind of employee this identity belongs to
    employee_type = models.CharField(
        max_length=50,
        choices=EmployeeType.choices,
    )

    # primary key of the employee row (corp_admins.id, loc_admins.id, location_users.id)
    employee_ref_id = models.PositiveIntegerField()

    # AD-related metadata
    ad_dn = models.CharField(max_length=255, null=True, blank=True)
    ad_guid = models.CharField(max_length=255, null=True, blank=True)
    ad_status = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "identity_registry"

    def __str__(self) -> str:
        return f"{self.eid} ({self.employee_type})"
