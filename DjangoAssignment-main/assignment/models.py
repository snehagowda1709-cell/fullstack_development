import uuid
from django.db import models
from django.utils import timezone
from academics.models import Course  # change if assignment's FK points elsewhere

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=255, default="default_assignment_name")
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, null=True)
    # Add your other fields here
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    # ... (more fields as needed)
    
    def __str__(self):
        return self.assignment_name

