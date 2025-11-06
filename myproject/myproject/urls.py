"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from basic.views import sample
from basic.views import sample1
from basic.views import sampleInfo
from basic.views import dynamicResponse
from basic.views import add
from basic.views import sub
from app.views import example
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path('53r54r',sample1),
    path('info',sampleInfo),
    path('dynamic',dynamicResponse),
    path('add',add),
    path('sub',sub),
    path('sam',example)
    
]
