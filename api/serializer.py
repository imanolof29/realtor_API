from rest_framework import serializers
from api.models import RealtorsList, RealtorDetails


class RealtorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtorsList
        fields = '__all__'


class RealtorDetailsSerializer(serializers.ModelSerializer):

    commercialdataid = RealtorsListSerializer()

    class Meta:
        model = RealtorDetails
        fields = '__all__'