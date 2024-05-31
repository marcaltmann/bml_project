import os
from pathlib import Path
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.shortcuts import render

# Load settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()


def index(request):
    return render(request, "index.html")


urlpatterns = [
    path('', index),
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()
