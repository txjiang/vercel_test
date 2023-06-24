# example/urls.py
from django.contrib import admin
from django.urls import path
from example.views import index, upload_file

urlpatterns = [
    #path('', index),
    path('admin/', admin.site.urls),
    path('upload/', upload_file),
]