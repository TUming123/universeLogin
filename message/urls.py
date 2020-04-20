"""message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import xadmin

from apps.messageForm.views import messageForm
from apps.messageForm.views import FormLoginView
from apps.messageForm.views import formLogin
from apps.messageForm.views import formSign
from apps.blog.views import blog
from apps.tips.views import tips, tipsLogin, tipsSign, TipsLoginView
from apps.universe.views import universe, universeLogin, universeSign, universeLoginView
from apps.auth.views import auth
from apps.grant.views import grant
from apps.serv.views import serv

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    path('messageForm/', messageForm, name="messageForm"),
    path('formLogin/', FormLoginView.as_view(), name="formLogin"),
    path('formSign/', formSign, name="formSign"),

    path('blog/', blog, name="blog"),

    path('tips/', tips, name="tips"),
    path('tipsLogin/', TipsLoginView.as_view(), name="tipsLogin"),
    path('tipsSign/', tipsSign, name="tipsSign"),

    path('universe/', universe, name="universe"),
    path('universeLogin/', universeLoginView.as_view(), name="universeLogin"),
    path('universeSign/', universeSign, name="universeSign"),

    path('', TemplateView.as_view(template_name="home.html"), name="home"),

    path('auth/', auth, name="auth"),
    path('grant/', grant, name="grant"),
    path('serv/', serv, name="serv"),

]
