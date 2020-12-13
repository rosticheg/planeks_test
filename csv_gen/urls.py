from django.conf.urls import url, include
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^new_schema/$', views.new_schema, name='new_schema'),
    url(r'^generate/$', views.generate, name='generate'),
    url(r'^check_scheme/$', views.check_scheme, name='check_scheme'),
    url(r'^my_schemas/$', views.my_schemas, name='my_schemas'),
    url(r'^(?P<s_id>\d+)/del', views.del_scheme, name='del_view'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


