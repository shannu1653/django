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


#3.class creating for signup page
class Users(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    
#4.class creating for movie details
class Movie(models.Model):
    Movie_name=models.CharField(max_length=100,unique=True)
    Date=models.DateField()
    Budget=models.CharField(max_length=100)
    Rating = models.CharField(max_length=10)



