from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, InventoryMovementViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"movements", InventoryMovementViewSet, basename="movements")

urlpatterns = router.urls