# -*- coding: utf-8 -*
import time
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from models import Users

def global_setting(request):
    return locals()


@csrf_exempt
def signup(request):
    context = {}
    return render(request, 'extra-signup.html', context)

@csrf_exempt
def registerzc(request):
    try:
        users = Users.objects.all()
        if users.filter(phone=request.POST['phone']):
            context = {'info': '手机号已存在！'}
        else:
            ob = Users()
            ob.username = request.POST['username']
            ob.name = request.POST['firstname'] + request.POST['lastname']
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password']))
            ob.password = m.hexdigest()
            ob.phone = request.POST['phone']
            ob.email = request.POST['email']
            ob.state = 1
            ob.addtime = time.time()
            ob.save()
            context = {'info': '添加成功！'}
    except:
        context = {'info': '添加失败！'}
        return render(request, "extra-signup.html", {"context": context})

    return redirect('/signin')