from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView   # Authentication




urlpatterns = [
    path('', views.index),
    path('index1/', views.index1),
    #path('students/', views.students),                     # using vicky CRUDS
    #path('students/<int:id>', views.students),             # using vicky CRUDS
    path('students/', views.StudentModelView.as_view()),     # django4kids: from rest_framework.views import APIView (views.py using class and CRUD methods in that class)
    path('students/<int:id>', views.StudentModelView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),          # Authentication
]
