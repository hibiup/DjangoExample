"""DjangoExamples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url


# 引入缺省 /index url
from . import index

# 引入 app1 模块，为避免歧义，改名为 app1
from app1.views import index as sample_app

urlpatterns = [
    path('admin/', admin.site.urls),

    # 缺省 /index url
    url(r'^$', index.index),

    # app/index url
    path('app/', sample_app.hello)
]

