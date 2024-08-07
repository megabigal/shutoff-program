from django.urls import path
from . import views

urlpatterns = [
    path('', views.m, name='page'),
    path('subwayStation/', views.index, name='subwayStation'),
    path('updateCheckbox/', views.updateCheckbox, name='updateCheckbox'),]