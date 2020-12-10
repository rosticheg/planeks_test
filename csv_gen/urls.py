from django.conf.urls import url, include
from . import views
from django.urls import path
#from .views import UserDashboard


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
#    url(r'^dashboard/$', UserDashboard.as_view(), name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
]


