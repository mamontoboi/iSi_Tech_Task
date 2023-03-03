from django.contrib import admin
from django.utils.html import format_html

from .models import Participants, Thread, Message


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_threads')
    ordering = ['id']

    def display_threads(self, obj):
        threads = obj.threads.all()
        return ", ".join([str(thread) for thread in threads])

    display_threads.short_description = 'Threads'


admin.site.register(Participants, ParticipantsAdmin)


class MessageInline(admin.StackedInline):
    model = Message
    extra = 1

    raw_id_fields = ['sender']


class ThreadAdmin(admin.ModelAdmin):
    inlines = [MessageInline]

    def display_participants(self, obj):
        participants = obj.participants.all()
        return ", ".join([participant.name for participant in participants])

    display_participants.short_description = 'participants'

    list_display = ('id', 'display_participants', 'created', 'updated')
    list_filter = ('created', 'updated')
    raw_id_fields = ('participants',)


class MessageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False # Disable the ability to add a new Message from the MessageAdmin form

    def has_change_permission(self, request, obj=None):
        return False # Disable the ability to edit a Message from the MessageAdmin form

    list_display = ['id', 'sender', 'thread', 'created', 'is_read']
    list_filter = ('sender', 'thread', 'is_read')


admin.site.register(Message, MessageAdmin)
admin.site.register(Thread, ThreadAdmin)

