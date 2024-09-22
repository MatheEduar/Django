from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name='posts'),
    path("<slug>", views.post, name='post')
]