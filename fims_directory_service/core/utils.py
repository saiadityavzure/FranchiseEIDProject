import random


def build_eid(first_name: str, last_name: str) -> str:
    """
    EID pattern:
        first initial + first 4 letters of last name + 3 digits
        Chris Smith -> csm it347 -> csm it347 (without space)
    """
    first_initial = first_name[0].lower() if first_name else "x"

    ln = (last_name or "user").replace(" ", "").lower()
    ln4 = (ln[:4]).ljust(4, "x")

    number = random.randint(100, 999)

    return f"{first_initial}{ln4}{number}"


def generate_unique_eid(first_name: str, last_name: str, max_attempts: int = 50) -> str:
    """
    Generate an EID that is globally unique using IdentityRegistry.
    """
    from fims_core.models import IdentityRegistry  # local import to avoid circular

    for _ in range(max_attempts):
        eid = build_eid(first_name, last_name)
        if not IdentityRegistry.objects.filter(eid=eid).exists():
            return eid

    raise ValueError("Could not generate a unique EID after many attempts.")
