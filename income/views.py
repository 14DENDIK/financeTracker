from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum

from .models import Income
from .forms import IncomeForm


class IncomePieChartView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        incomes = Income.objects.values('type__name').annotate(earned_money=Sum('amount')).filter(user=request.user)
        for income in incomes:
            labels.append(income['type__name'])
            data.append(income['earned_money'])
        return JsonResponse({
            'labels': labels,
            'data': data,
        })

    def post(self, request, *args, **kwargs):
        labels = []
        data = []
        form = IncomeForm(request.user, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            incomes = Income.objects.values('type__name').annotate(earned_money=Sum('amount')).filter(user=request.user)
            for income in incomes:
                labels.append(income['type__name'])
                data.append(income['earned_money'])
            user_total_income = request.user.total_income
            return JsonResponse({
                'is_valid': True,
                'labels': labels,
                'data': data,
                'user_total_income': user_total_income
            })
        else:
            return JsonResponse({
                'is_valid': False,
                'error': 'Invalid form field',
            })
