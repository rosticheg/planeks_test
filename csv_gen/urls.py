from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^new_schema/$', views.new_schema, name='new_scema'),
    url(r'^generate/$', views.generate, name='generate'),
    path('accounts/', include('django.contrib.auth.urls')),
]


