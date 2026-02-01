from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    content = models.TextField(max_length = 400)
    number = models.IntegerField(max_length = 13)