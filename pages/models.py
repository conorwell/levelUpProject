from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Summary(models.Model):
    title = models.CharField
    text = models.CharField
    summary = models.CharField