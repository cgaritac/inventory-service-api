from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, InventoryMovement
from .serializers import ProductSerializer, InventoryMovementSerializer

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
    
class InventoryMovementViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryMovementSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        return InventoryMovement.objects.filter(
            company=self.request.user.company
        )
    
    def perform_create(self, serializer):
        serializer.save()