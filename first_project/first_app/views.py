from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # each view must return an HTTPResponse
    return HttpResponse("Hello, world!")
