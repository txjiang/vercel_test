# example/urls.py
from django.contrib import admin
from django.urls import path
from example.views import index, process_the_upload_file

urlpatterns = [
    path('', index),
    path('upload/', process_the_upload_file),
]