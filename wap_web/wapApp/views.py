# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.shortcuts import render,HttpResponse,render_to_response,redirect
from .models import Users as User
import json
from django.contrib import messages
from django.conf import settings as django_settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'../templates/wapApp/base/index.html')
def contact(request):
    return render(request,'../templates/wapApp/contact.html')
def photos(request):
    return render(request,'../templates/wapApp/photos.html')
def about(request):
    return render(request,'../templates/wapApp/about.html')
def features(request):
    return render(request,'../templates/wapApp/features.html')


def ditu(request):
    return render(request,'../templates/wapApp/ditu.html')

def user(request):
    return render(request,'../templates/wapApp/userCenter.html')
def base(request):
    return render(request,'../templates/wapApp/base.html')
def personalCenter(request):
    return render(request,'../templates/wapApp/personalCenter.html')
#注册
def redirectreg(request):
    return render(request, '../templates/wapApp/base/register.html')
def regist(request):
    user = User.objects.filter(username=request.POST['username'])
    if user.exists():
        return HttpResponse('{"status":"fail","msg":"注册失败，用户名已注册"}')
    else:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        add_date = int(time.time())
        user = User.objects.create(username=username, password=password,email=email, add_date=add_date)
        user.is_active = 0

        # user.active_date = 0
        user.save()
        sendEmail(user)
        return HttpResponse('{"status":"success","msg":"用户注册成功"}')

def sendEmail(user):
    import smtplib
    from email.mime.text import MIMEText
    mail_host = "smtp.163.com"
    mail_user = "15805156299@163.com"
    mail_pass = "lsiya19950109"
    user_id = str(user.id)
    # username=username.encode('utf-8')
    sender = "15805156299@163.com"
    receivers = [user.email]
    content ="\n".join([u'{0},欢迎加入minio掌上商城'.format(user.username), u'请访问该链接，完成用户验证:',
	        '/'.join([django_settings.DOMAIN,'activate?id='+user_id]),u'有效激活时间是4小时内'])
    title = '激活您的掌上商城账号'
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = '掌上商城邮箱管理员'+'<'+sender+'>'
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
def activate(request):
    # request.encoding = 'gb2312'
    user_id = int(request.GET['id'])
    # username = username.encode('utf-8')
    # import urllib.parse
    # username = urllib.parse.unquote(request.GET.get('username'),'GBK')
    # print(username)
    user_info = User.objects.get(id=user_id)
    return render(request,'../templates/wapApp/base/activate.html',{'user_info':user_info})
def activeUser(request):#激活时要确定激活的id,完善激活的严谨性
    # active_date = timezone.now()
    # User.objects.filter(id=1).update(is_active=1)
    user_info = User.objects.get(id=int(request.GET.get('user_id')))
    if(int(time.time()) > (user_info.add_date+4*24*60*3600)):
        return HttpResponse('{"status":"overtime","msg":"激活连接失效，请重新注册"}')
    else:
        user = User.objects.get(id=request.GET.get('user_id'))
        user.is_active = 1
        user.active_date = int(time.time())
        user.save()
        return HttpResponse('{"status":"activesuccess","msg":"激活成功"}')
# 登录
def redirectlog(request):
    return render(request, '../templates/wapApp/base/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        info = User.objects.filter(username=username, password=password)
        is_active = User.objects.filter(username=username, is_active=1)
        if info.exists() and is_active.exists():
            info_dict = {'username': username}
            request.session['username'] = username
            return HttpResponse('{"status":"success"}')

        else:
            return HttpResponse('{"status":"error","msg":"登录失败"}')
    else:
        return HttpResponse('{"status":"fail","msg":"登录失败，用户名或密码错误"}')

# 登出
def logout(request):
    # request.session.set_expiry(value)过期时间
    # 如果value是一个整数，会话将在value秒没有活动后过期。
    # 如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
    # 如果value为None，那么会话永不过期。
    request.session.clear()
    return render(request, '../templates/wapApp/userCenter.html')

# 账户安全界面
def security(request):

    return render(request,'../templates/wapApp/security.html')

