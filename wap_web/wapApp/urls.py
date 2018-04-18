from django.conf.urls import url

from . import views
app_name = 'wapApp'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^user/$', views.user, name='user'),
    url(r'^base/$', views.base, name='base'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^photos/$', views.photos, name='photos'),
    url(r'^about/$', views.about, name='about'),
    url(r'^features/$', views.features, name='features'),
    url(r'^ditu/$', views.ditu, name='ditu'),#index可以去掉吗
    url(r'^regist/',views.regist,name='regist'),
    url(r'^redirectreg/',views.redirectreg,name='redirectreg'),
    url(r'^redirectlog/',views.redirectlog,name='redirectlog'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^activate/$', views.activate, name='activate'),
    url(r'^activeUser/$', views.activeUser, name='activeUser'),
    url(r'^security/$', views.security, name='security'),
    url(r'^personalCenter/$', views.personalCenter, name='personalCenter'),

]
