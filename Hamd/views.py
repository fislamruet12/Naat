from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Artist,Album
# Create your views here.

def album_list(request):
    artists=Artist.objects.all()
    template=loader.get_template('Hamd/album_list.html')
    xll=[1 ,2,3,4,5,6]
    context={
        'artists':artists,
        'xll':xll
    }
    return HttpResponse(template.render(context,request))

def artist_song(request,artist_id,album_id):
    album=Album.objects.get(pk=album_id)

    ori_artist=Artist.objects.get(pk=artist_id)
    al_album=ori_artist.album_set.all

    template=loader.get_template('Hamd/artist_song.html')
    get_artist=artist_id
    get_album=album_id
    context={
        'album':album,
        'get_artist':get_artist,
        'get_album=':get_album,
        'al_album':al_album
    }
    return HttpResponse(template.render(context,request))

def like(request,artist_id,album_id):
    album=Album.objects.get(pk=album_id)

    ori_artist = Artist.objects.get(pk=artist_id)
    al_album = ori_artist.album_set.all

    a=album.likes
    a=a+1
    album.likes=a
    album.save()
    get_artist = artist_id
    get_album = album_id

    template=loader.get_template('Hamd/artist_song.html')
    context={
        'album':album,
        'get_artist': get_artist,
        'get_album=': get_album,
        'al_album': al_album
    }
    return HttpResponse(template.render(context,request))

