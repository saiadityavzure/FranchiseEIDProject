from django.db import models
from core.models.base import BaseModel
from core.models.user_fields_mixin import BaseUserFieldsMixin
from .company import Company
from .location import Location
from .identity_registry import IdentityRegistry

class LocationUser(BaseModel, BaseUserFieldsMixin):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="location_users"
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="location_users"
    )

    @property
    def eid(self):
        ident = IdentityRegistry.objects.filter(
            employee_type=IdentityRegistry.EmployeeType.LOCATION_USER,
            employee_ref_id=self.id
        ).first()
        return ident.eid if ident else None

    class Meta:
        db_table = "location_users"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.location.code})"
