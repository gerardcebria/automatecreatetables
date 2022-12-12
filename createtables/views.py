from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import DataBaseProject

from createtables.forms import tableBaseForm


def index(request):
    context = {'form' : tableBaseForm()}
    
    return render(request, 'index.html', context)



def ProcessColumns(request):
    if request.method == 'POST':
        form = tableBaseForm(request.POST)
        context = {}
        if form.is_valid():
            context['server'] = form.cleaned_data['server']
            context['source'] = form.cleaned_data['source']
            context['key_columns'] = form.cleaned_data['key_columns'].split(',')
            context['columns'] = form.cleaned_data['columns'].split(',')
        
        db_info = DataBaseProject.objects.filter(auto_increment_id = context['server'])
        # print(context)
        for db in db_info:
            print(db.username)

        return render(request, 'process.html', context)