from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=10)
    scroe = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

class Comments(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=200)
    score = models.IntegerField()