from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from apps.companies.models import Company

class User(AbstractUser):
    class Role(models.TextChoices):
        OWNER = "OWNER", "Owner"
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        EMPLOYEE = "EMPLOYEE", "Employee"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(
        Company, 
        on_delete=models.CASCADE, 
        related_name="users",
        null=True,
        blank=True
    )
    role = models.CharField(
        max_length=20, 
        choices=Role.choices, 
        default=Role.EMPLOYEE
    )

    def __str__(self):
        return f"{self.username} - {self.company}"
    