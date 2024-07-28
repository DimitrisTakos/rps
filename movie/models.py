from django.conf import settings
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    production_date = models.DateTimeField(blank=True,null=True)
    duration = models.IntegerField()
    grade = models.FloatField()
    zip_file = models.FileField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


