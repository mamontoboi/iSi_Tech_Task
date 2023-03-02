"""isitech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('create_user/', views.ParticipantsFormView.as_view(), name='create_user'),
    path('create_user_int/', views.create_participant, name='create_user_int'),
    path('all_users/', views.get_all_participants, name='all_users'),
    path('', views.get_all_threads, name='all_threads'),
    path('success_creation/', views.success_creation, name='success'),
    path('success_deletion/', views.success_thread_deletion, name='success_thread_delete'),
    path('create_thread/', views.ThreadFormView.as_view(), name='create_thread'),
    path('get_or_create_thread/<str:name_1>&<str:name_2>/', views.get_or_create_thread, name='get_or_create_thread'),
    path('delete_thread/<int:thread_id>/', views.delete_thread, name='delete_thread'),
    path('threads_for_user/<str:user_name>/', views.threads_for_user, name='threads_for_user'),
    path('messages_for_thread/<int:thread_id>/', views.messages_for_thread, name='messages_for_thread'),
    path('check_message/<int:message_id>/', views.check_message, name='check_message'),
    path('create_message/', views.create_message, name='create_message'),

]
