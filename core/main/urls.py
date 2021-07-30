from django.urls import include, path
from . import views
from core import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('addAttendance/', views.addAttendance, name='addAttendance'),
    path('addMarks/', views.addMarks, name='addMarks'),
    path('addNotice/', views.addNotice, name='addNotice'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
]