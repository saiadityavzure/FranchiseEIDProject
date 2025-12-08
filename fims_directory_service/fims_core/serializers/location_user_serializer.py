from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models.location_user import LocationUser
from fims_core.models.company import Company
from fims_core.models.location import Location
from fims_core.serializers.company_serializer import CompanySerializer
from fims_core.serializers.location_serializer import LocationSerializer


class LocationUserSerializer(BaseSerializer):
    """
    Serializer for Location Users (store-level employees).
    Includes:
      - BaseUserFieldsMixin fields
      - company & location (read + write)
      - eid from IdentityRegistry (read-only)
    """

    # READ-ONLY nested objects
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    company_id = serializers.IntegerField(source="company.id", read_only=True)
    location_id = serializers.IntegerField(source="location.id", read_only=True)

    # EID from IdentityRegistry property
    eid = serializers.CharField(read_only=True)

    # WRITE-ONLY input foreign keys
    company_input = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        source="company",
        write_only=True,
    )

    location_input = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location",
        write_only=True,
    )

    class Meta(BaseSerializer.Meta):
        model = LocationUser
        fields = BaseSerializer.Meta.fields + [
            # BaseUserFieldsMixin
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "uid_expiry_date",

            # FKs (read)
            "company",
            "company_id",
            "location",
            "location_id",

            # FKs (write)
            "company_input",
            "location_input",

            # computed
            "eid",
        ]
