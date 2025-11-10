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


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from basic.views import sample
from basic.views import sample1
from basic.views import sampleInfo
from basic.views import dynamicResponse
from basic.views import add
from basic.views import sub
from app.views import example
from basic.views import health
from basic.views import addStudent
from basic.views import post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path('53r54r',sample1),
    path('info',sampleInfo),
    path('dynamic',dynamicResponse),
    path('add',add),
    path('sub',sub),
    path('sam',example),
    path('health',health),
    path('addstudent/',addStudent),
    path('post/',post),
    path("admin/", admin.site.urls),
    path('insta/', include('insta.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
 ] # <-- login/logout URLs

# serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)