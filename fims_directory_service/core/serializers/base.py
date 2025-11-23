from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Shared base serializer for:
    - created_at / updated_at timestamps
    - status
    - created_by / last_updated_by
    """

    class Meta:
        # These will be extended in child serializers via `fields + [...]`
        fields = [
            "id",
            "created_at",
            "updated_at",
            "status",
            "created_by",
            "last_updated_by",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "last_updated_by",
        ]
