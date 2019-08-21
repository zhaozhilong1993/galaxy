# -*- coding: utf-8 -*
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from models import Users

def global_setting(request):
    return locals()


def signout(username):
    pass



@csrf_exempt
def index(request):
    context = {}
    # signin_check
    context['username'] = request.session['username']
    return render(request, 'index.html', {'context': context})

def calendar(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'page-calendar.html', context)

def item(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'page-blog-item.html', context)

def test(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'test.html', context)
