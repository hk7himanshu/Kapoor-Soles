from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('home', views.index, name="homepage"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('men', views.men, name="men"),
    path('women', views.women, name="women"),
    path('kids', views.kids, name="kids")
]
