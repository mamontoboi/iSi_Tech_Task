from isiapp.models import Participants, Message, Thread
from rest_framework import viewsets
from .serializers import ParticipantsSerializer, ThreadSerializer, MessageSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination


class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    pagination_class = LimitOffsetPagination
    max_limit = 50




