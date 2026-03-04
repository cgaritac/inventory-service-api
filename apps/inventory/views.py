from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, InventoryMovement
from .serializers import ProductSerializer, InventoryMovementSerializer
from apps.users.permissions import IsOwnerOrAdmin
from apps.users.permissions import IsManagerOrAbove
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permissions_classes = [IsAuthenticated]

    filterset_fields = ["minimum_stock", "is_active"]
    search_fields = ["name", "sku"]
    ordering_fields = ["created_at", "quantity", "name"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Product.objects.filter(
            company=self.request.user.company
        )
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permissions_classes = [IsAuthenticated, IsOwnerOrAdmin]
        elif self.action == 'destroy':
            permissions_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            permissions_classes = [IsAuthenticated]
        return [permission() for permission in permissions_classes]
    
class InventoryMovementViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryMovementSerializer
    permissions_classes = [IsAuthenticated]

    filterset_fields = ["movement_type", "product"]
    ordering_fields = ["created_at", "quantity"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return InventoryMovement.objects.filter(
            company=self.request.user.company
        )
    
    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated, IsManagerOrAbove]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save()