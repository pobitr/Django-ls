from django.urls import path
from django.contrib import admin
from polls import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contect/', views.con, name='con'),
    path('about/', views.about, name='about'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    # path('data', views.testing, name='testing'),
]