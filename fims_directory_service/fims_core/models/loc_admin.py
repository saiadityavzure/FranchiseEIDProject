from django.db import models
from core.models.base import BaseModel
from core.models.user_fields_mixin import BaseUserFieldsMixin
from .company import Company
from .location import Location
from .identity_registry import IdentityRegistry

class LocAdmin(BaseModel, BaseUserFieldsMixin):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="loc_admins"
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="loc_admins"
    )

    @property
    def eid(self):
        ident = IdentityRegistry.objects.filter(
            employee_type=IdentityRegistry.EmployeeType.LOC_ADMIN,
            employee_ref_id=self.id
        ).first()
        return ident.eid if ident else None

    class Meta:
        db_table = "loc_admins"

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Loc Admin - {self.location.code})"
