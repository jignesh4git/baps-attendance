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
from django.contrib import admin
from attendance.views import  index
from material.frontend import urls as frontend_urls
from django.contrib.auth import views as auth
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),     
    url('^$', index, name="index"),
    url(r'', include(frontend_urls)),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^baps/login/$', auth.login, {'template_name': 'attendance/login.html'}, name='login'),
    url(r'^baps/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
]
