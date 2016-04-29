from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
    title = models.TextField(default='')
    brief = models.TextField(default='')
    owner = models.ForeignKey(User,default=None)

class Chapter(models.Model):
    subtitle = models.TextField(default='')
    content = models.TextField(default='')
    story = models.ForeignKey(Story, default=None)
    writter = models.ForeignKey(User, default=None)

