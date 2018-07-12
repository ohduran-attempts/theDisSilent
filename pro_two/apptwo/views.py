from django.shortcuts import render
#from django.http import HttpResponse
#from apptwo.models import User
from apptwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'apptwo/index.html')

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid Form')

    return render(request, 'apptwo/users.html', context={'form':form})
