from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(primary_key=True, max_length=64)
    release_date = models.DateField()
    duration = models.IntegerField()
    plot = models.CharField(max_length=512)
    
    # director = models.CharField(max_length=64, foreign_ke)
    # language
    # genre
    # actor
    def __str__(self):
        return self.title
    
class Actor(models.Model):
    ...
    
class Director(models.Model):
    ...
    
class Language(models.Model):
    ...
    
class Genre(models.Model):
    ...    
    
class Rating(models.Model):
    ...
    
class Review(models.Model):
    ...
    