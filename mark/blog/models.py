from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50,default='标题')
    content=models.TextField(null=True)
