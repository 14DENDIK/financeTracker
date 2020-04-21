from django.urls import path
from . import views

app_name = 'income'

urlpatterns = [
    path('income-pie-chart', views.IncomePieChartView.as_view(), name='income-pie-chart'),
]
