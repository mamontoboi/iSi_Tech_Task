from isiapp.models import Participants, Thread, Message
from rest_framework import serializers


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
