from django.db import transaction
from core.utils import generate_unique_eid
from fims_core.models import IdentityRegistry


def create_identity_for_employee(instance, employee_type: str) -> IdentityRegistry:
    """
    Creates an IdentityRegistry entry for the given employee instance.

    - Generates a globally unique EID
    - Stores employee_type and employee_ref_id
    - Leaves AD fields empty for now (to be filled by AD sync)
    """

    if not instance.id:
        raise ValueError("Employee instance must be saved before identity creation.")

    # Check if identity already exists (idempotent)
    existing = IdentityRegistry.objects.filter(
        employee_type=employee_type,
        employee_ref_id=instance.id,
    ).first()
    if existing:
        return existing

    eid = generate_unique_eid(instance.first_name, instance.last_name)

    with transaction.atomic():
        identity = IdentityRegistry.objects.create(
            eid=eid,
            employee_type=employee_type,
            employee_ref_id=instance.id,
            ad_status="Pending",
        )
    return identity
