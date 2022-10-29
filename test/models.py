from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    test=models.CharField(blank=False,null=False,max_length=5)

