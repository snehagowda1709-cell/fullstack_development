import json
import uuid
from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

class PrimaryAuditModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        abstract = True

class TimeAuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UserAuditModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_%(class)s_set',
        on_delete=models.SET_NULL, null=True, blank=True)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='updated_%(class)s_set',
        on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        abstract = True

class AbstractModel(PrimaryAuditModel, TimeAuditModel, UserAuditModel):
    history = HistoricalRecords(inherit=True)
    class Meta:
        abstract = True
        ordering = ['-created_at']
