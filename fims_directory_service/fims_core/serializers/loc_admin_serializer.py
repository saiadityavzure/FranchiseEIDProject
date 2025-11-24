from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models.loc_admin import LocAdmin
from fims_core.models.company import Company
from fims_core.models.location import Location
from fims_core.serializers.company_serializer import CompanySerializer
from fims_core.serializers.location_serializer import LocationSerializer


class LocAdminSerializer(BaseSerializer):
    """
    Serializer for Location Administrators.
    - Includes BaseUserFieldsMixin fields
    - Supports company & location read/write
    - Includes EID from IdentityRegistry (read-only)
    """

    # ---------- READ-ONLY FIELDS ----------
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    company_id = serializers.IntegerField(source="company.id", read_only=True)
    location_id = serializers.IntegerField(source="location.id", read_only=True)

    eid = serializers.CharField(read_only=True)

    # ---------- WRITE-ONLY INPUT FIELDS ----------
    company_input = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        source="company",
        write_only=True
    )

    location_input = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location",
        write_only=True
    )

    class Meta(BaseSerializer.Meta):
        model = LocAdmin

        fields = BaseSerializer.Meta.fields + [
            # BaseUserFieldsMixin
            "first_name",
            "last_name",
            "email",
            "phone_number",

            # FK (READ)
            "company",
            "company_id",
            "location",
            "location_id",

            # FK (WRITE)
            "company_input",
            "location_input",

            # From IdentityRegistry
            "eid",
        ]
