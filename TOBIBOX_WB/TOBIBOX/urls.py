from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('post/<str:id>', views.post, name='post'),
    path('constructor', views.constructor, name='constructor'),
    path('draw/<str:id>', views.draw, name='draw'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', views.user_logout, name='logout'),

]
