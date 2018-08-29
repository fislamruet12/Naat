from django.db import models
from time import time

def get_upload_file(instance,filename):
    return "%s_%s"%(str(time()).replace('.','_'),filename)

class Artist(models.Model):
    artist_name=models.CharField(max_length=200,null=False)
    artist_about=models.CharField(max_length=1000,null=False)
    artist_photo=models.FileField(upload_to=get_upload_file,null=True)
    genre=models.CharField(null=True,max_length=100)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    album_title = models.CharField(max_length=200)
    album_logo=models.FileField(upload_to=get_upload_file)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.album_title



class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_name=models.FileField(upload_to=get_upload_file)

    def __str__(self):
        return self.song_title;


