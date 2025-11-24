from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models.company import Company
from fims_core.models.country import Country
from fims_core.serializers.country_serializer import CountrySerializer


class CompanySerializer(BaseSerializer):
    # -----------------------------
    # READ-ONLY: For GET responses
    # -----------------------------
    # Return the nested country object
    country = CountrySerializer(read_only=True)

    # Return the FK ID cleanly for frontend use
    country_id = serializers.IntegerField(
        source="country.id",
        read_only=True
    )

    # -----------------------------
    # WRITE-ONLY: For POST / PUT / PATCH
    # -----------------------------
    # Accept a country ID as input
    country_input = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
        source="country"   # binds to same FK field
    )

    class Meta(BaseSerializer.Meta):
        model = Company
        fields = BaseSerializer.Meta.fields + [
            "name",
            "address",
            "city",
            "state",

            # READ FIELDS
            "country",      # nested object
            "country_id",   # ID only

            # WRITE FIELD
            "country_input",

            "comp_code",
        ]
