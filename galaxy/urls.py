from django.contrib import admin
from django.conf.urls import url

from earth.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # web index
    url(r'^galaxy/index/$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),

    # web login
    url(r'^login/$', login, name='login'),

    # web signup
    url(r'^signup/$', signup, name='signup'),

    # web user profile
    url(r'^profile/$', profile, name='profile'),

    # web user list
    url(r'^userlist/$', userlist, name='userlist'),
]