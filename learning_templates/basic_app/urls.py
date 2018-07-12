from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

url_patterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
