from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def index(request):
    return JsonResponse({
  "apiversion": "1",
  "author": "MyUsername",
  "color": "#888888",
  "head": "default",
  "tail": "default",
  "version": "0.0.1-beta"
})
