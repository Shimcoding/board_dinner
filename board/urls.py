from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views

app_name='board'
urlpatterns = [
    path('', views.index,name='index'),
    path('create', views.create,name='create'),
    path('detail/<num>', views.detail,name='detail'),
    path('delete/<conid>', views.delete,name='delete'),
    path('update/<conid>', views.update,name='update'),
    path('up/<conid>/<st>', views.up, name='up'),
    path('create_reply/<conid>', views.create_reply, name='create_reply'),
    path('agree/<num>/<conid>', views.agree, name='agree'),
]
