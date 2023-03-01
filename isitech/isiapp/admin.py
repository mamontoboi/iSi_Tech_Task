from django.contrib import admin
from django.utils.html import format_html

from .models import Participants, Thread, Message


class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    ordering = ['id']


admin.site.register(Participants, ParticipantsAdmin)


class MessageInline(admin.StackedInline):
    model = Message
    extra = 1


class ThreadAdmin(admin.ModelAdmin):
    inlines = [MessageInline]
    exclude = ('messages',) # Exclude the messages field from the ThreadAdmin form


class MessageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False # Disable the ability to add a new Message from the MessageAdmin form

    def has_change_permission(self, request, obj=None):
        return False # Disable the ability to edit a Message from the MessageAdmin form


admin.site.register(Message, MessageAdmin)
admin.site.register(Thread, ThreadAdmin)

