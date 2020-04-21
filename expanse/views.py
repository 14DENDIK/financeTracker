from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Sum

from .models import Expanse
from .forms import ExpanseForm


class ExpansePieChartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        expanses = Expanse.objects.values('type__name').annotate(spent_money=Sum('amount')).filter(user=request.user)
        for expanse in expanses:
            labels.append(expanse['type__name'])
            data.append(expanse['spent_money'])
        return JsonResponse({
            'labels': labels,
            'data': data,
        })

    def post(self, request, *args, **kwargs):
        labels = []
        data = []
        form = ExpanseForm(request.user, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            expanses = Expanse.objects.values('type__name').annotate(spent_money=Sum('amount')).filter(user=request.user)
            for expanse in expanses:
                labels.append(expanse['type__name'])
                data.append(expanse['spent_money'])
            user_total_expanse = request.user.total_expanse
            return JsonResponse({
                'is_valid': True,
                'labels': labels,
                'data': data,
                'user_total_expanse': user_total_expanse
            })
        else:
            return JsonResponse({
                'is_valid': False,
                'error': 'Incorrect Form'
            })


class InformationView(View):

    def get(self, request, *args, **kwargs):
        expanses = Expanse.objects.filter(user=request.user)
        return render(request, 'expanse_income/information.html', {})
