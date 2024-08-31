from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.m, name='page'),
    path('accounts/login/', views.m, name='page'),
    path('subwayStation/', views.index, name='subwayStation'),
    path('updateCheckbox/', views.updateCheckbox, name='updateCheckbox'),
    path('logPage/',views.logView, name='logPage'),
    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
  path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),]