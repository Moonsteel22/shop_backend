from django.db import models
from django.contrib.auth.models import User as IUser

class User(IUser):
    phone = models.CharField(max_length=11, blank=True)
    age = models.PositiveIntegerField(default=0)
    img_url = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=2, default='U', blank=True)

    class Meta:
        managed = True


