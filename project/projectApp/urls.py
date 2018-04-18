from django.conf.urls import url

from . import views
app_name = 'projectApp'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^ditu/$', views.ditu, name='ditu'),
]
