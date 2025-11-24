from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models.location import Location
from fims_core.models.company import Company
from fims_core.serializers.company_serializer import CompanySerializer


class LocationSerializer(BaseSerializer):
    # READ-ONLY
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(source="company.id", read_only=True)

    # WRITE-ONLY
    company_input = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        source="company"
    )

    class Meta(BaseSerializer.Meta):
        model = Location
        fields = BaseSerializer.Meta.fields + [
            "code",
            "name",

            # read
            "company",
            "company_id",

            # write
            "company_input",
        ]
