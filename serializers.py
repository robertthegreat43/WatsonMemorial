from rest_framework import serializers

from .models import Events, Pastor, LocalScripture


class PastorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pastor
        fields = ['name', 'prayer', 'email', 'audio_segment']


class EventsSerializer(serializers.ModelSerializer):

            class Meta:
                model = Events
                fields = ['event_name', 'event_date', 'event_description', 'event_location', 'event_image']





class LocalScriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalScripture
        fields = ['topic', 'reference', 'reflection', 'created_at', 'updated_at']


class ListVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date', 'event_description', 'event_location', 'event_image']