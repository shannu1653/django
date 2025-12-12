from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from basic.views import Signup,Movies,create_credit_card


# ✅ Home Page (shows all links)
def home(request):
    return render(request, "home.html")

# ✅ Import basic app views
from basic.views import (
    sample, sample1, sampleInfo, dynamicResponse,
    add, sub, health, addStudent,post, login, getAllUsers
)

from app.views import example

from emotionapp import views

urlpatterns = [
    # ✅ HOME PAGE
    path('', home, name='home'),

    # ✅ Admin URL (only one)
    path('admin/', admin.site.urls),

    # ✅ Basic app URLs
    path('greet/', sample),
    path('53r54r/', sample1),
    path('info/', sampleInfo),
    path('dynamic/', dynamicResponse),
    path('add/', add),
    path('sub/', sub),
    path('sam/', example),
    path('health/', health),
    path('addstudent/',addStudent),
    path('post/', post),

    # ✅ Insta app URLs
    path('insta/', include('insta.urls')),

    # ✅ Django login / logout pages
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',Signup),
    path('login/',login),
    path('users/', getAllUsers),
    path('creadit/', create_credit_card),

    #movies
    path('movies/',Movies),

    path('', views.upload_page),
    path('predict/', views.predict_emotion),


]

# ✅ MEDIA (needed for image display)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
