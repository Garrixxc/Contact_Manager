from django.db import models
from datetime import datetime

class Member(models.Model):
    firstname=models.CharField(max_length=100)
    num=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    notes=models.CharField(max_length=300)
    createdTime = models.DateTimeField(default=datetime.now, null=True)