"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from evdetest import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # Bu urlin sonuna yagmur yazinca gelecek html sayfa
    # Templates klasoru altinda eklersin eger views.login ustunde ctrl ile sol tusa basarsan views altindaki login fonksiyonu icindeki blogu isletir ve hello html sayfasina yonelir
    url(r'^yagmur/', views.login),
    url(r'^nedemek$', views.nebu)
]
