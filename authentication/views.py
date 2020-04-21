from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User
from .forms import UserLoginForm, UserRegisterForm
from expanse.models import Expanse
from expanse.forms import ExpanseForm
from income.models import Income
from income.forms import IncomeForm


class HomeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        expanse_form = ExpanseForm(request.user)
        income_form = IncomeForm(request.user)
        context = {
            'url_name': 'home',
            'expanse_form': expanse_form,
            'income_form': income_form,
        }
        return render(request, 'auth/home.html',  context)


class UserLoginView(View):

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            'form': form
        }
        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.GET.get('next', 'auth:home'))
                else:
                    messages.error(request, 'Your account is disabled.')
                    return redirect('auth:home')
            else:
                messages.warning(request, 'Not existing user.')
                return redirect('auth:login')
        else:
            messages.error(request, 'Not correct input field(s).')
            return redirect('auth:login')


class UserRegisterView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('auth:register')
            return redirect('auth:home')

class UserLogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('auth:login')
