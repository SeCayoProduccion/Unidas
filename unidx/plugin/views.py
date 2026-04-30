from django.shortcuts import render
from django.http import HttpResponse
from .models import Flux
from datetime import datetime
#Imports del form
from django.views.generic import View
from .forms import MyUserForm

# Create your views here.
def index(request):
    data = Flux.objects.values()

    now = datetime.now()
    flux = Flux(now, 1.0, "hello")
    flux.save()

    return HttpResponse(data, content_type='application/json')

#parte del form

def MyUserView(View):
	form_class = MyUserForm
	template_name = 'books/api.html'


	return HttpResponse(data, content_type = 'application/json')
