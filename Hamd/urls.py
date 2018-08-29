from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'^$',views.artist_song,name="artist_song"),
    url(r'^$',views.album_list,name="album_list"),
    url(r'^(?P<album_id>[0-9]+)/$',views.artist_song,name="artist_song"),
    url(r'^like/(?P<artist_id>[0-9]+)/(?P<album_id>[0-9]+)/$',views.like,name="like"),
    url(r'^(?P<artist_id>[0-9]+)/(?P<album_id>[0-9]+)/$',views.artist_song,name="artist_song"),

]