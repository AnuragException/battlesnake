from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', index),
]

urlpatterns = format_suffix_patterns(urlpatterns)