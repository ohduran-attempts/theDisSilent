from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'text':'Hello, world',
    'number':101,
    }
    return render(request, 'basic_app/index.html', context)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
