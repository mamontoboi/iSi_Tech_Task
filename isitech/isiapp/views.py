from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ParticipantsModelForm, ThreadModelForm, MessageFormModel
from .models import Participants, Thread, Message


def success_creation(request):
    """Notification in case of successful creation of a new element."""
    return HttpResponse(f"<script>alert ('The operation was successfully performed!'); "
                        "window.location = '/';</script>")


class ParticipantsFormView(FormView):
    form_class = ParticipantsModelForm
    template_name = 'form_view.html'
    success_url = reverse_lazy("app:success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_all_participants(request):
    participants = Participants.get_all()
    print(participants)
    return render(request, 'list_participants.html', {'data': participants})


def create_participant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        participant = Participants.objects.create(name=name)
        participant.save()
        return redirect(reverse_lazy('app:all_users'))
    else:
        return redirect(reverse_lazy('app:all_users'))


class ThreadFormView(FormView):
    form_class = ThreadModelForm
    template_name = 'new_thread_view.html'
    success_url = reverse_lazy("app:success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def get_all_threads(request):
    threads = list(Thread.objects.all())
    return render(request, 'list_threads.html', {'data': threads})


def create_thread(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        participant = Participants.objects.create(name=name)
        participant.save()
        return redirect(reverse_lazy('app:success'))
    else:
        return redirect(reverse_lazy('app:all_users'))


def get_or_create_thread(request, name_1, name_2):
    thread = Thread.get_or_create_thread(name_1, name_2)
    return render(request, 'list_threads.html', {'data': thread})


def threads_for_user(request, user_name):
    user = Participants.objects.get(name=user_name)
    threads = user.list_of_threads()
    return render(request, 'list_threads_for_user.html', {'data': threads, 'name': user_name})


def messages_for_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    messages = thread.messages.all()
    return render(request, 'list_messages_for_thread.html', {'data': messages, 'thread': thread_id})


def success_thread_deletion(request):
    """Notification in case of successful deletion of the author."""
    return HttpResponse("<script>alert ('The thread was successfully deleted!'); "
                        "window.location = '/';</script>")


def delete_thread(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if thread:
        thread.delete()
        return redirect(reverse_lazy('app:success_thread_delete'))
    else:
        return HttpResponse("<script>alert ('The thread with this number does not exist'); "
                        "window.location = '/';</script>")


def check_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.is_read = True
    message.save()
    return render(request, 'message_details.html', {'message': message})


def create_message(request):
    if request.method == 'POST':
        form = MessageFormModel(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            thread = data.get('thread')
            return HttpResponse(f"<script>alert ('The message was successfully created'); "
                                f"window.location = '/messages_for_thread/{thread.id}';</script>")
        else:
            print(form.errors)

    else:
        form = MessageFormModel()
    return render(request, 'new_message.html', {'form': form})