from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dictionary = {
        'insert_me': "Hello, I am from views.py",
    }
    return render(request, 'apptwo/help.html', context=my_dictionary)
