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
    duration = models.IntegerField()
    grade = models.FloatField()
    cheatsheet = models.ForeignKey('Cheatsheet',null=True,on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Cheatsheet(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='cheatsheets/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

