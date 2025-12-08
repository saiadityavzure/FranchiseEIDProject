from rest_framework import serializers
from core.serializers.base import BaseSerializer
from fims_core.models.corp_admin import CorpAdmin
from fims_core.models.company import Company
from fims_core.serializers.company_serializer import CompanySerializer


class CorpAdminSerializer(BaseSerializer):
    # READ
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(source="company.id", read_only=True)
    eid = serializers.CharField(read_only=True)

    # WRITE
    company_input = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
        source="company"
    )

    class Meta(BaseSerializer.Meta):
        model = CorpAdmin
        fields = BaseSerializer.Meta.fields + [
            # BaseUserFieldsMixin fields:
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "uid_expiry_date",
            # "title",

            # FK
            "company",
            "company_id",
            "company_input",

            # Computed from IdentityRegistry
            "eid",
        ]
