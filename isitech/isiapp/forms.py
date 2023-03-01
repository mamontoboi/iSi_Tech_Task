from django import forms
from .models import Participants, Thread, Message


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

