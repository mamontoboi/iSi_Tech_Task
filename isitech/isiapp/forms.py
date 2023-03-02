from django import forms
from .models import Participants, Thread, Message
from urllib.parse import urlparse
from django.core.exceptions import ValidationError


class URLFormField(forms.URLField):
    def validate(self, value):
        super().validate(value)
        parsed_url = urlparse(value)
        if not parsed_url.scheme or not parsed_url.netloc or not parsed_url.path:
            raise ValidationError("Invalid URL format")


class ParticipantsModelForm(forms.ModelForm):
    url = URLFormField()

    class Meta:
        model = Participants
        fields = ["id", "name"]


class ThreadModelForm(forms.ModelForm):
    url = URLFormField()

    class Meta:
        model = Thread
        fields = ["id", 'participants']


class MessageFormModel(forms.ModelForm):
    url = URLFormField()

    class Meta:
        model = Message
        fields = ["id", "sender", "thread", "text"]

