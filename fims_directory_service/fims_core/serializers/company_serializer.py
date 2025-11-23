from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models import Company


class CompanySerializer(BaseSerializer):
    """
    Serializer for Company model.
    Inherits audit/status fields from BaseSerializer.
    """

    # If you want to return country as nested object later,
    # we can customize here. For now, keep it as PK.

    class Meta(BaseSerializer.Meta):
        model = Company
        fields = BaseSerializer.Meta.fields + [
            "name",
            "address",
            "city",
            "state",
            "country",    # FK -> Country (as id)
            "comp_code",
        ]
