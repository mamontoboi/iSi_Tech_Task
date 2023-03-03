from isiapp.models import Participants, Thread, Message
from rest_framework import serializers


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = ('id', 'name')

    def validate(self, data):
        # Check if the email is already taken
        if Participants.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError('This name is already taken')

        return data


class ThreadSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Participants.objects.all(),
        required=True
    )

    class Meta:
        model = Thread
        fields = ('id', 'participants', 'created', 'updated')

    def validate(self, data):
        if len(data['participants']) != 2:
            raise serializers.ValidationError('The thread must contain two participants.')

        return data


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, data):
        thread = Thread.objects.get(id=data['thread'].id)
        sender = Participants.objects.get(id=data['sender'].id)
        if sender not in thread.participants.all():
            raise serializers.ValidationError('This sender is not a participant in this thread')

        return data
