from rest_framework import serializers
from .models import Artist, Music



from rest_framework import serializers
from .models import Artist, Music



# class ArtistListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Artist
#         fields = ('id','name',)


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicListSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'name', 'music_set',)

class MusicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'name', 'artist',)
        read_only_fields = ('artist',)




# class MusicListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Music
#         fields = ('id','title',)






# class ArtistDetailSerializer(serializers.ModelSerializer):
#     music_set = MusicListSerializer(many=True, read_only=True)

#     class Meta:
#         model = Artist
#         fields = '__all__'
        


# class MusicDetailSerializer(serializers.ModelSerializer):

#     class Meta:
        
#         model = Music
#         fields = ('id', 'title', 'artist')
#         read_only_fields = ('artist',)



