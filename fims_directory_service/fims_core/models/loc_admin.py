from django.db import models
from django.core.exceptions import ValidationError
from core.models.base import BaseModel
from core.models.user_fields_mixin import BaseUserFieldsMixin
from .company import Company
from .location import Location
from .identity_registry import IdentityRegistry


class LocAdmin(BaseModel, BaseUserFieldsMixin):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="loc_admins",
        db_index=True
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="loc_admins",
        db_index=True
    )

    @property
    def eid(self):
        ident = IdentityRegistry.objects.filter(
            employee_type=IdentityRegistry.EmployeeType.LOC_ADMIN,
            employee_ref_id=self.id
        ).first()
        return ident.eid if ident else None

    def clean(self):
        """
        Ensure location belongs to the given company.
        """
        if self.location.company_id != self.company_id:
            raise ValidationError("Selected location does not belong to this company.")

    class Meta:
        db_table = "loc_admins"
        constraints = [
            # Prevent duplicate loc admin email for same location
            models.UniqueConstraint(
                fields=["location", "email"],
                name="uniq_loc_admin_email_per_location"
            )
        ]

        indexes = [
            models.Index(fields=["company"], name="idx_locadmin_company"),
            models.Index(fields=["location"], name="idx_locadmin_location"),
            models.Index(fields=["email"], name="idx_locadmin_email"),
        ]

    def __str__(self):
        fname = self.first_name or ""
        lname = self.last_name or ""
        return f"{fname} {lname} (Loc Admin - {self.location.code})".strip()
