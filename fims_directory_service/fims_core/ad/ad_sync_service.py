from fims_core.ad.ldap_client import ADClient
from fims_core.models import IdentityRegistry


def sync_employee_to_ad(instance, employee_type: str, ident: IdentityRegistry):
    """
    Creates the AD user for CorpAdmin, LocAdmin, or LocationUser.
    Stores DN + GUID + AD Status in IdentityRegistry.
    """

    # If AD already created, skip
    if ident.ad_dn:
        return

    ad = ADClient()

    if not ad.connect():
        ident.ad_status = "ConnectionFailed"
        ident.save()
        return

    try:
        result = ad.create_user(
            employee_type=employee_type,
            eid=ident.eid,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email or f"{ident.eid}@adtest.local",
            password="TempPass@123",
        )

        ident.ad_dn = result["dn"]
        ident.ad_guid = result["guid"]
        ident.ad_status = "Created"
        ident.save()

    except Exception as e:
        ident.ad_status = f"Failed: {str(e)}"
        ident.save()
