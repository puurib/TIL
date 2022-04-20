from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Artist, Music
from .serializers import (
    ArtistListSerializer, 
    ArtistSerializer, 
    MusicListSerializer, 
    MusicSerializer
)
from music import serializers

# Create your views here.

@api_view(['GET','POST'])
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)  #many=True 까먹음
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def artist_detail(request, artist_pk):
    # artist = get_object_or_404(pk=artist_pk)
    # serializer = ArtistSerializer(artist)
    # return Response(serializer.data)


# @api_view(['POST'])
# def music_create(request, artist_pk):
    #artist = get_object_or_404(pk=artist_pk)
    #serializer = MusicListSerializer(data=request.data)
    #if serializer.is_valid(raise_exception=True):
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)