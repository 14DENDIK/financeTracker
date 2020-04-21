from django.urls import path
from . import views

app_name = 'expanse'

urlpatterns = [
    path('expanse-pie-chart/', views.ExpansePieChartView.as_view(), name='expanse-pie-chart'),
    path('information/', views.InformationView.as_view(), name='information'),
]
