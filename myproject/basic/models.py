from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)


#2.class creating post data with fields
class PostData(models.Model):
    post_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=50)
    post_date = models.DateField()       
    post_description = models.CharField(max_length=1000)  # ✅ FIXED
