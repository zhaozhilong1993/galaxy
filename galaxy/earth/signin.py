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
def signin(request):
    context = {}
    return render(request, 'extra-signin.html', context)

# 登陆操作
@csrf_exempt
def logindl(request):
    try:
        user = Users.objects.get(username=request.POST['username'])
        # 根据账号获取登陆着信息
        m = hashlib.md5()
        m.update(bytes(request.POST['password']))
        if user.password == m.hexdigest():
            # 若此处登陆成功，将 当前登陆信息放到session中，并跳转页面
            request.session['username'] = user.username
            request.session['uid'] = user.id
            request.session['phone'] = user.phone
            return redirect(reverse('index'))
        else:
            context = {'info': '登陆密码出错！'}
            return render(request, "extra-signin.html", context)

    except:
        context = {'info': '账号不存在！'}
        return render(request, "extra-signin.html", context)