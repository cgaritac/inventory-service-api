# Product Model

from django.db import models
import uuid
from apps.companies.models import Company

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name="products"
    )
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)

    class Meta:
        unique_together = ("company", "sku")
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["sku"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.company.name})"


# InventoryMovement Model

from django.core.exceptions import ValidationError
from django.conf import settings

class InventoryMovement(models.Model):
    class MovementType(models.TextChoices):
        IN = "IN", "Stock Entry"
        OUT = "OUT", "Stock Exit"
        ADJUSTMENT = "ADJUSTMENT", "Manual Adjustment"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="movements"    
    )
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name="movements"
    )
    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices
    )
    quantity = models.IntegerField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="movements_created"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="movements_updated"
    )
    deleted_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="movements_deleted"
    )

    class Meta:
        indexes = [
            models.Index(fields=["company"]),
            models.Index(fields=["product"]),
            models.Index(fields=["created_at"]),
        ]

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        
        if self.movement_type == self.MovementType.OUT:
            if self.product.quantity < self.quantity:
                raise ValidationError("Insufficient stock.")
    
    def save(self, *args, **kwargs):
        self.full_clean()

        if not self.pk:
            if self.movement_type == self.MovementType.IN:
                self.product.quantity += self.quantity
            elif self.movement_type == self.MovementType.OUT:
                self.product.quantity -= self.quantity
            elif self.movement_type == self.MovementType.ADJUSTMENT:
                self.product.quantity = self.quantity

            self.product.save()

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.movement_type} - {self.product.name}"