from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'INJECTION'
        return context
