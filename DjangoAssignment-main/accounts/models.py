from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from Basefolder.models import AbstractModel

class Professor(AbstractUser, AbstractModel):
    is_professor = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='professors',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='professor',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='professors',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='professor',
    )

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    def __str__(self):
        # Display username for easy admin panel debug, or change to name/email
        return self.username

class Profil(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return self.name
