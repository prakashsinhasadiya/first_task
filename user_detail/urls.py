# -*- coding: utf-8 -*-
import os


from django.conf.urls import url
from django.contrib.auth.views import logout


from .views import UserDetail,delete,edit


urlpatterns = [

    url(r'^$', UserDetail.as_view(), name='userdetail'),
    url(r'^delete/$',delete, name="delete"),
    url(r'^edit/$',edit,name="edit"),
    

]
