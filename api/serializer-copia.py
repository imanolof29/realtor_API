
from api.models import Realtors, Realtors_list, Realtors_detail
from rest_framework import serializers

#
# class SongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = ('id', 'name')
#
#
# class ArtistSerializer(serialisers.ModelSerializer):
#     songs = SongSerializer(many=True)
#
#     class Meta:
#         model = Artist
#         fields = ('id', 'name', 'songs')



class Realtor_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Realtors_list
        fields = ('position')


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtors_detail
        fields = ('commercialdataid','id_name', 'street','zipcode')
        # fields = '__all__'

    print('hello_3')

