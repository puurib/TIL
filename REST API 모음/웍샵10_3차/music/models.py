from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __self__(self):
        return self.name


class Music(models.Model):
    # ForeignKey(참조 외래키, on_delete속성)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __self__(self):
        return self.title
        