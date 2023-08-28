from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('record/<int:pk>', views.patient_record, name='record'),
    path('mainpage/', views.mainPage, name='mainpage'),
    path('deleterecord/<int:pk>', views.deleterecord, name='deleterecord'),
    path('addpatient/', views.addpatient, name='addpatient'),

]
