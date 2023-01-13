from django.db import models
class list(models.Model):
    Name=models.CharField(max_length=400)
    Price=models.TextField()
    Stock=models.IntegerField()
    Price=models.IntegerField()
    Image=models.CharField(max_length=8000)
# Create your models here.
