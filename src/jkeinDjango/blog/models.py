from django.db import models
import datetime
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=20)
    name_slug = models.SlugField(primary_key=True)

    def __unicode__(self):
        return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    cat = models.ForeignKey(Category)
    published = models.DateTimeField(default=datetime.datetime.now())
    writer = models.CharField(max_length=30, default=settings.WRITER)
    slug = models.SlugField(primary_key=True)
    imagefile = models.CharField(max_length=300, default=image.name, blank=True)
    
    def __unicode__(self):
        return self.title