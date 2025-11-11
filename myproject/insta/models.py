from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    location = models.CharField(max_length=100, blank=True, null=True)
    tag_people = models.CharField(max_length=100, blank=True, null=True)
    mood = models.CharField(max_length=50, blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
