from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    production_date = models.DateTimeField(blank=True,null=True)
    duration = models.DateTimeField()
    grade = models.FloatField()
    imdb = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
