from django.db import models
from django.db.models.fields import DateField, DateTimeField
from taggit.manager import TaggableManager

# Create your models here.
class log(models.Model):
    title
    date
    content
    datetime = DateTimeField()
    tags = TaggableManager()

