from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('mainpage/', views.mainPage, name='mainpage'),

]
