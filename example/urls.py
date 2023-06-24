# example/urls.py
from django.urls import path
from example.views import index, upload_file

urlpatterns = [
    path('', index),
    path('upload/', upload_file),
]