from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, InventoryMovement
from .serializers import ProductSerializer, InventoryMovementSerializer
from apps.users.permissions import IsOwnerOrAdmin

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(
            company=self.request.user.company,
            is_active=True
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

    def get_queryset(self):
        return InventoryMovement.objects.filter(
            company=self.request.user.company
        )
    
    def perform_create(self, serializer):
        serializer.save()