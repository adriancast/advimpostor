from django.db import models
from taggit.managers import TaggableManager
from datetime import datetime

from django.utils import timezone
# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    text = models.TextField(blank=True)
    iframe = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts-images/', blank=True)
    image_alt = models.CharField(max_length=512, blank=True)

    author = models.CharField(max_length=512)

    tags = TaggableManager()

    def __str__(self):
        return str(self.title)


class Visit(models.Model):
    date = models.DateTimeField(default=timezone.now())
    page_name = models.CharField(max_length=512)

    def __str__(self):
        return self.page_name
