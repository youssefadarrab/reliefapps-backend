from rest_framework import serializers
from reliefapp.models import Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('VideoId',
                  'VideoLink',
                  'VideoTimestamp')
