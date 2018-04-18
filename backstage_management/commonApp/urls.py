from django.conf.urls import url

from . import views
app_name = 'commonApp'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),

]
