from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    BASE_USER = 'base'
    ADMIN_USER = 'admin'
    ROLE_CHOICES = [
        (BASE_USER, 'Base User'),
        (ADMIN_USER, 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
class Candidate(models.Model):
    
    dec_choice = [
        ('Yes','Yes'),
        ('No','No')
    ]
    
    username = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True)
    decision = models.CharField(max_length=10,choices=dec_choice)
    status = models.CharField(max_length=50, default='awaiting permission')
    
    def __str__(self) -> str:
        return self.username
    
    def save(self, *args, **kwargs):
        if self.decision == 'Yes':
            self.status = 'value updated'
        else:
            self.status = 'awaiting permission'
        super().save(*args, **kwargs)