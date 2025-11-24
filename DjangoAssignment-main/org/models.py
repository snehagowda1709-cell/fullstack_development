import uuid
from django.db import models
from django.utils import timezone
from Basefolder.models import AbstractModel  # if used as your project indicates

class Organization(AbstractModel):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, null=True)
    # Add any other organization fields you require
    
    def __str__(self):
        return self.name
