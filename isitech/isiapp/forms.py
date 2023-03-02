from django import forms
from .models import Participants, Thread, Message
from urllib.parse import urlparse
from django.core.exceptions import ValidationError


class ParticipantsModelForm(forms.ModelForm):

    class Meta:
        model = Participants
        fields = ["id", "name"]


class ThreadModelForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ["id", 'participants']


class MessageFormModel(forms.ModelForm):

    class Meta:
        model = Message
        fields = ["id", "sender", "thread", "text"]

