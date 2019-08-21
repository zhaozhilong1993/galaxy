# -*- coding: utf-8 -*
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from models import Users

def global_setting(request):
    return locals()


@csrf_exempt
def notebook_list(request):
    context = {}
    return render(request, 'notebook-list.html', {'context': context})

@csrf_exempt
def notebook_edit(request):
    context = {}
    return render(request, 'notebook-edit.html', {'context': context})

@csrf_exempt
def notebook(request):
    context = {}
    return render(request, 'notebook.html', {'context': context})