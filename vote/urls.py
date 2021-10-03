
from django.contrib import admin
from django.urls import path,include
from . import views

app_name="vote"
urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('detail/<num>', views.detail, name="detail"),
    path('vote/<conid>', views.vote, name="vote"),
]
