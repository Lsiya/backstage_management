# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'../templates/projectApp/index.html')
def ditu(request):
    return render(request,'../templates/projectApp/ditu.html')
