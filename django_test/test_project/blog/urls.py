from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-post', views.new_post, name='new_post')
]