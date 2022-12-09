from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render

from createtables.forms import tableBaseForm

import logging

def index(request):
    context = {'form' : tableBaseForm()}
    
    return render(request, 'index.html', context)



def ProcessColumns(request):
    if request.method == 'POST':
        form = tableBaseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['server'])
            print(form.cleaned_data['source'])
            print(form.cleaned_data['key_columns'])
            print(form.cleaned_data['columns'])
        logging.debug("Log message goes here.")

        return render(request, 'process.html', {})