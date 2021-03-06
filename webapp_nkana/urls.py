"""webapp_nkana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapp_nkana import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^volunteer/', include('volunteer.urls')),
    url(r'^mentor/', include('mentor.urls')),
    url(r'^insights/', 'webapp_nkana.views.insights'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^login/$', 'webapp_nkana.views.app_login'),
    url(r'^rest/insights', views.RestInsights.as_view()),
    url(r'^$', 'webapp_nkana.views.index', name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)