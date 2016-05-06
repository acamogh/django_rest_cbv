from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models




# Create your models here.
class Design(models.Model):
    user = models.ForeignKey(User)
    tag_name = models.CharField(max_length=100)
    theme_name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)

    def __unicode__(self):
        return self.user.username