from django.db.models.signals import post_save
from django.dispatch import receiver

from fims_core.identity import create_identity_for_employee
from fims_core.models import (
    CorpAdmin,
    LocAdmin,
    LocationUser,
    IdentityRegistry,
)


@receiver(post_save, sender=CorpAdmin)
def create_identity_for_corp_admin(sender, instance: CorpAdmin, created: bool, **kwargs):
    if not created:
        return

    create_identity_for_employee(
        instance,
        employee_type=IdentityRegistry.EmployeeType.CORP_ADMIN,
    )


@receiver(post_save, sender=LocAdmin)
def create_identity_for_loc_admin(sender, instance: LocAdmin, created: bool, **kwargs):
    if not created:
        return

    create_identity_for_employee(
        instance,
        employee_type=IdentityRegistry.EmployeeType.LOC_ADMIN,
    )


@receiver(post_save, sender=LocationUser)
def create_identity_for_location_user(sender, instance: LocationUser, created: bool, **kwargs):
    if not created:
        return

    create_identity_for_employee(
        instance,
        employee_type=IdentityRegistry.EmployeeType.LOCATION_USER,
    )
