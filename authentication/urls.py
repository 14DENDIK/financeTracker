from django.urls import path

from . import views

app_name = 'auth'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/register/', views.UserRegisterView.as_view(), name='register'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
]
