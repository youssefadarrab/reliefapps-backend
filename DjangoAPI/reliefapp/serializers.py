from rest_framework import serializers
from reliefapp.models import History, Bookmark

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('HistoryId',
                  'HistoryLink',
                  'HistoryTimestamp')

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('BookmarkId',
                  'BookmarkLink')
