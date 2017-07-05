# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.contrib.auth.views import *
#from .forms import MyAuthenticationForm

urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls
    url(r'^login/$',
        login, name='login'),

    url(r'^logout/$',
        logout,
        name='logout'),
    url(r'^logout-then-login/$',
        logout_then_login,
        name='logout_then_login'),

    url(r'^main/$',
        views.principal,
        name='principal'),

    url(r'^contact/$',
        views.contact,
        name='contact'),

    url(r'^product/$',
        views.product,
        name='product'),

    url(r'^services/$',
        views.services,
        name='services'),

    url(r'^about/$',
        views.aboutus,
        name='about'),

    url(r'^$', views.dashboard, name='dashboard'),

    # change password urls
    url(r'^password-change/$',
        password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        password_change_done,
        name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$',
        password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),

    url(r'^register/$', views.register, name='register'),


]


