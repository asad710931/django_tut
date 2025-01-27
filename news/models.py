from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    title = models.CharField(max_length=100)
    des = HTMLField()
# Create your models here.
