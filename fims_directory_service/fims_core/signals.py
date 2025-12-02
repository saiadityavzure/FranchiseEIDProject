from django.db.models.signals import post_save
from django.dispatch import receiver

from fims_core.identity import create_identity_for_employee
from fims_core.ad.ad_sync_service import sync_employee_to_ad
from fims_core.models import (
    CorpAdmin,
    LocAdmin,
    LocationUser,
    IdentityRegistry,
)


@receiver(post_save, sender=CorpAdmin)
def handle_corp_admin(sender, instance, created, **kwargs):
    if created:
        ident = create_identity_for_employee(
            instance, IdentityRegistry.EmployeeType.CORP_ADMIN
        )
        sync_employee_to_ad(instance, IdentityRegistry.EmployeeType.CORP_ADMIN, ident)


@receiver(post_save, sender=LocAdmin)
def handle_loc_admin(sender, instance, created, **kwargs):
    if created:
        ident = create_identity_for_employee(
            instance, IdentityRegistry.EmployeeType.LOC_ADMIN
        )
        sync_employee_to_ad(instance, IdentityRegistry.EmployeeType.LOC_ADMIN, ident)


@receiver(post_save, sender=LocationUser)
def handle_location_user(sender, instance, created, **kwargs):
    if created:
        ident = create_identity_for_employee(
            instance, IdentityRegistry.EmployeeType.LOCATION_USER
        )
        sync_employee_to_ad(instance, IdentityRegistry.EmployeeType.LOCATION_USER, ident)
