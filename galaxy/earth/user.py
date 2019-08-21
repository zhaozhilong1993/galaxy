# -*- coding: utf-8 -*
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from models import Users

def global_setting(request):
    return locals()

def user_profile(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'user-profile.html', context)

def user_list(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'user-list.html', context)
