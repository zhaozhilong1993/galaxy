from django.contrib import admin
from django.conf.urls import url

from earth.views import *
from earth.signin import *
from earth.signup import *
from earth.myclass import *
from earth.notebooks import *
from earth.system import *
from earth.user import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # web index
    url(r'^galaxy/index/$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^$', index, name='index'),

    # web login
    url(r'^login/$', signin, name='signin'),
    url(r'^logindl/$', logindl, name='logindl'),

    # web signup
    url(r'^signup/$', signup, name='signup'),
    url(r'^signup/registerzc/$', registerzc, name='registerzc'),


    # web user list
    url(r'^user/profile/$', user_profile, name='user_profile'),
    url(r'^user/list/$', user_list, name='user_list'),


    # web page calendar
    url(r'^calendar/$', calendar, name='calendar'),

    # web page item
    url(r'^item/$', item, name='item'),

    # web Linux learning page
    url(r'^classlist/$', classlist, name='classlist'),
    url(r'^myclass/$', myclass, name='myclass'),
    url(r'^mywork/$', mywork, name='mywork'),

    # web note page
    url(r'^notebook/list/$', notebook_list, name='notebook_list'),
    url(r'^notebook/edit/$', notebook_edit, name='notebook_edit'),
    url(r'^notebook/$', notebook, name='notebook'),

    # web system control page
]
