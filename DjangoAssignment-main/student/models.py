from django.db import models
from Basefolder.models import AbstractModel

class Student(AbstractModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

