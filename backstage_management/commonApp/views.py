# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, render_to_response
from django import forms
from django.http.response import HttpResponseRedirect
import re
# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                               error_messages={ 'invalid': "用户名不能超过10位字符"})
    password = forms.CharField(label='密  码', widget=forms.PasswordInput,
                               error_messages={'invalid': '密码不能超过15字符'})

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
def index(request):
    return render(request, '../templates/commonApp/index.html')
def login(request):
    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            userJudge = User.objects.filter(username=username,password=password)
            if userJudge:
                response = HttpResponseRedirect('/')
                response.set_cookie('cookie_username', username, 300)
                return response
            else:
                return render(request, '../templates/commonApp/fixLogin.html', {'uf': uf, 'error': "用户名或密码错误"})
    else:
        uf = LoginForm()
        return render(request, '../templates/commonApp/fixlogin.html', {'uf': uf})

def regist(request):
    Method = request.method
    if Method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            User.objects.create(username=username, password=password,email=email)
            User.save()
            return render(request, '../templates/commonApp/fixLogin.html')
        else:
            uf = UserForm()
        return render(request, '../templates/commonApp/index.html', {'uf': uf})
def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('cookie_username')
    return response