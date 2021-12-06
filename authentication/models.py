from django.db import models
from django.contrib.auth.models import AbstractUser

from logisticapp.models import Department

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    is_semisuper = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_deprtment = models.ForeignKey(to=Department, null=True, related_name='staffs_in_department', on_delete=models.CASCADE)
    
    # user_deprtment = models.CharField(max_length=200, null=True)

    # avatar = models.ImageField(null=True, default="avatar.svg")

    
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username