from django.shortcuts import render

# Create your views here.
 
def global_setting(request):
    return locals()


def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'extra-signin.html', context)

def signup(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'extra-signup.html', context)

def profile(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'extra-profile.html', context)

def userlist(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'extra-user-list.html', context)