from django.contrib import admin
from django.urls import path,include
from.import views



urlpatterns = [
    path('', views.Teacher_detail, name='Teacher_detail'),
    path('teacher_profile/<pk>/',views.teacher_profile,name='teacher_profile'),
    path('teacher_add_sv/',views.teacher_add_sv,name='teacher_add_sv'),
    
    
]
