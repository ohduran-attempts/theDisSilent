from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = form.FormName()
    return render(request, 'basicapp/forms.html', {'form':form})
