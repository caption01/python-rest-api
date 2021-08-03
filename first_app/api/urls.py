from django.conf.urls import url
from django.urls import path

from .views import first_function

urlpatterns = [
    url('first/', first_function, name='first'),
]
