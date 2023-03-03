from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Participants(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True, default='John Doe')

    class Meta:
        verbose_name_plural = "Participants"

    def __str__(self):
        return self.name

    def list_of_threads(self):
        threads = Thread.objects.filter(participants=self)
        last_messages = []
        for thread in threads:
            number = thread.messages.filter(is_read=False).count()
            last_message = thread.messages.last()
            if last_message:
                last_messages.append((thread.id, last_message.id,  last_message.sender, last_message.text,
                                      last_message.is_read, number))
            else:
                last_messages.append((thread.id,))

        return last_messages

    def number_of_unread_messages(self):
        return Message.objects.filter(thread__participants=self, is_read=False).exclude(sender=self).count()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return list(Participants.objects.all())


class Thread(models.Model):
    participants = models.ManyToManyField(Participants, related_name='threads')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Threads'

    def __str__(self):
        return str(self.pk)

    def add_participant(self, participant_id):
        participant = Participants.objects.get(id=participant_id)
        if self.participants.count() < 2:
            self.participants.add(participant)
        else:
            return {'error': 'Only two participants!'}

    @staticmethod
    def get_or_create_thread(name_1, name_2):
        try:
            user_1 = Participants.objects.get(name=name_1)
            user_2 = Participants.objects.get(name=name_2)
        except ObjectDoesNotExist:
            return ["Participant of participants does not exist!"]
        thread = Thread.objects.filter(participants=user_1).filter(participants=user_2).first()
        if thread:
            return [thread]
        else:
            new_thread = Thread.objects.create()
            new_thread.participants.add(user_1, user_2)
            return [new_thread]

    @staticmethod
    def delete_thread(thread_id):
        thread = Thread.objects.get(id=thread_id)
        thread.delete()
        return True

    def get_messages(self):
        messages = self.messages.all()
        if messages.filter(is_read=True).exists():
            return f"Some of messages have been read: {messages}"
        else:
            return f"None of messages have been read: {messages}"

    def create_message(self, sender, text):
        participant = Participants.objects.get(name=sender)
        message = Message(sender=participant, text=text, thread=self, is_read=False)
        message.save()


class Message(models.Model):
    sender = models.ForeignKey(Participants, related_name='sent_messages', on_delete=models.CASCADE, db_index=True)
    text = models.TextField(max_length=512, default='empty message')
    thread = models.ForeignKey(Thread, related_name='messages', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ['-is_read']

    def __str__(self):
        return f"Message {self.pk} from {self.sender}"

    def read(self):
        self.is_read = True
