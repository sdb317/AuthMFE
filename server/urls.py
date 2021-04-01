"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path, reverse
from rest_framework import routers

from . import userViewSet
from . import appView

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'users', userViewSet.UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    re_path('^$', appView.AppView.as_view()),
]