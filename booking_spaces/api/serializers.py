from booking.models import ParkingSpace, Schedule
from rest_framework import serializers


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ParkingSpace


class ListDatesSerializer(serializers.ModelSerializer):
    space = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=ParkingSpace.objects.all()
    )

    class Meta:
        fields = ('space', 'reserving_date',)
        model = Schedule
