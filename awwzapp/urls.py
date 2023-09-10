from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500
from app.views import *
from app import urls as appUrls

urlpatterns = [
    path('', index, name='index'), 
    path('', include(appUrls)),
    path('admin/', admin.site.urls), 

    path("user/register/", register, name="register"),
    path('home/', home, name='home'),
    path("user/", include('django.contrib.auth.urls')), 

    path('about', about, name = 'about'),
    path('contact', contact, name = 'contact'),
    path('terms', terms, name = 'terms'),
    path('policy', policy, name = 'policy'),
]

handler404 = error_404
handler500 = error_500