from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    url('add_task', views.add_task, name='add_task'),
    url('finish_task', views.finish_task, name='finish_task'),
    url('remove_task', views.remove_task, name='remove_task')
]