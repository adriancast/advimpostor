from django.db import models
from taggit.managers import TaggableManager

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
