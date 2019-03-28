from django.conf import settings
from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique_for_date=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    rec_date = models.DateTimeField(default=timezone.now)
    rec_mod_date = models.DateTimeField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()  # https://django-taggit.readthedocs.io/en/latest/index.html

    def __str__(self):
        return self.title

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
