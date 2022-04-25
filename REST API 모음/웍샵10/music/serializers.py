from rest_framework import serializers
from .models import Artist, Music

# 모든 가수정보
class ArtistListSerializer(serializers.Serializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

# 모든 음악정보
class MusicListSerializer(serializers.Serializer):
    class Meta:
        model = Music
        fields = ('id', 'title',)

# 상세 가수정보
class ArtistDetailSerializer(serializers.Serializer):
    music_set = MusicListSerializer(many = True, read_only =True)
    class Meta:
        model = Artist
        fields = ('id', 'name',)
        #fields = ('id', 'name', 'music_set',)

# 상세 음악정보
class MusicDetailSerializer(serializers.Serializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist',)