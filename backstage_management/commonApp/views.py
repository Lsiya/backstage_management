# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
# PIL是python2版本的图像处理库，不过现在用Pillow比PIL强大，是python3的处理库
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from io import BytesIO

from django.shortcuts import render, render_to_response
from django import forms
from django.http.response import HttpResponseRedirect
import re
from django.contrib.auth import authenticate
from .models import User
import django.utils.timezone as timezone

# Create your views here.
def index(request):
   if request.session.get('username'):
        return render(request, '../templates/commonApp/index.html')
   else:
       return render(request, '../templates/commonApp/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['userpwd']

        info = User.objects.filter(username=username, password=password)
        if info.exists():
            info_dict = {'username': username}
            request.session['username']=username
            return render(request, '../templates/commonApp/index.html',{'info_dict': info_dict})
        else:
            return render(request, '../templates/commonApp/login.html',{'errors': '用户名或密码不正确'})
    else:
        return render(request, '../templates/commonApp/login.html')
def regist(request):
    user = User.objects.filter(username=request.POST['user-name'])
    if user.exists():
        return render(request,'../templates/commonApp/index.html',{'errors': '用户已存在'})
    else:
        username = request.POST['user-name']
        password = request.POST['userpassword']
        sex = request.POST.get('sex')
        phone = request.POST['user-tel']
        email = request.POST['email']
        add_date = timezone.now()
        note = request.POST['note']
        admin_role = request.POST.get('admin-role')
        User.objects.create(username=username, password=password, sex=sex, phone=phone, email=email, add_date=add_date, note=note, admin_role=admin_role)
        return render('../templates/commonApp/login.html')
# def logout(request):



