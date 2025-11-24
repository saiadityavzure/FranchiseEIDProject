from django.db import models
from core.models.base import BaseModel
from core.models.user_fields_mixin import BaseUserFieldsMixin
from .company import Company
from .identity_registry import IdentityRegistry


class CorpAdmin(BaseModel, BaseUserFieldsMixin):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="corp_admins",
        db_index=True  # ⭐ (2) Improves query performance
    )

    @property
    def eid(self):
        ident = IdentityRegistry.objects.filter(
            employee_type=IdentityRegistry.EmployeeType.CORP_ADMIN,
            employee_ref_id=self.id
        ).first()
        return ident.eid if ident else None

    class Meta:
        db_table = "corp_admins"
        constraints = [
            # ⭐ (1) Prevent duplicate corporate admin email within a company
            models.UniqueConstraint(
                fields=["company", "email"],
                name="uniq_corp_admin_email_per_company"
            )
        ]

        # ⭐ (2) Add useful indexes for speed
        indexes = [
            models.Index(fields=["company"], name="idx_corpadmin_company"),
            models.Index(fields=["email"], name="idx_corpadmin_email"),
        ]

    def __str__(self):
        # ⭐ (4) Fallback safety if names are missing
        fname = self.first_name or ""
        lname = self.last_name or ""
        return f"{fname} {lname} (Corp Admin - {self.company.comp_code})".strip()
