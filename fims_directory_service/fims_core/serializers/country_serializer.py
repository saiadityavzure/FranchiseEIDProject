from rest_framework import serializers
from fims_core.models import Country

class CountrySerializer(serializers.ModelSerializer):
    continent_name = serializers.CharField(source="continent.name", read_only=True)

    class Meta:
        model = Country
        fields = ["id", "name", "code", "continent", "continent_name"]
