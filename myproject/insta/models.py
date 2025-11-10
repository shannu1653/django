from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_date = models.DateField()
    location = models.CharField(max_length=200, blank=True, null=True)

    # extra features
    is_public = models.BooleanField(default=True)       # public/private
    allow_comments = models.BooleanField(default=True)
    allow_sharing = models.BooleanField(default=True)
    mood = models.CharField(max_length=100, blank=True, null=True)
    tag_people = models.CharField(max_length=200, blank=True, null=True)

    image = models.ImageField(upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
