from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from createtables.forms import dataBaseForm


def index(request):
    context = {'form' : dataBaseForm()}
    
    return render(request, 'index.html', context)



