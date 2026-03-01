from rest_framework import serializers
from .models import Product, InventoryMovement

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "company", "created_at", "updated_at", "deleted_at")

class InventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = "__all__"
        read_only_fields = ("id", "company", "created_by", "updated_by", "deleted_by", "created_at", "updated_at", "deleted_at")

    def create(self, validated_data):
        request = self.context["request"]

        validated_data["company"] = request.user.company
        validated_data["created_by"] = request.user

        return super().create(validated_data)