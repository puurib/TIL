# vue router

```
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Movie


def Movie(request):
    pass
```

```
from django.urls import path
from . import views

app_name='Movies'

urlpatterns = [
    path('movies/', views.movies),
]
```

