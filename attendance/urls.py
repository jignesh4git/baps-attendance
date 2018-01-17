"""baps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views import generic
from .views import HaribhaktDetailListView,newHaribhakt,index,newKaryakarGroup,KaryakarGroupListView,editHaribhaktDetail,editKaryakarGroup,deleteHaribhaktDetail,deleteKaryakarGroup
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('^$', index, name="home"),
	url(r'^login/$',generic.TemplateView.as_view(template_name="attendance/login.html"),name="login"),
	url(r'^logout/$',auth.logout, name='/login/'),
    url(r'^users/change_password/$', login_required(auth.password_change),{'post_change_redirect': '/', 'template_name': 'change_password.html'}, name='change_password'),
    url(r'^haribhakt/new/$',newHaribhakt, name="newHaribhakt"),
    url(r'^haribhaktdetail/edit/(?P<haribhaktdetail_id>\d+)/$', editHaribhaktDetail, name='editHaribhaktDetail'),
    url(r'^haribhaktdetail/delete/(?P<haribhaktdetail_id>\d+)/$', deleteHaribhaktDetail, name='deleteHaribhaktDetail'),
    url(r'^haribhaktdetail/$', HaribhaktDetailListView.as_view(), name='haribhaktdetail-list'),
    url(r'^karyakargroup/new/$',newKaryakarGroup,name="newKaryakarGroup"),
    url(r'^karyakargroup/edit/(?P<karyakargroup_id>\d+)/$', editKaryakarGroup, name='editKaryakarGroup'),
    url(r'^karyakargroup/delete/(?P<karyakargroup_id>\d+)/$', deleteKaryakarGroup, name='deleteKaryakarGroup'),
    url(r'^karyakargroups/$', KaryakarGroupListView.as_view(), name='karyakargroup-list'),
]
