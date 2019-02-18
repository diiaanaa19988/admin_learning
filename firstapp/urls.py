from django.conf.urls import url

from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^course/$', views.courseListView.as_view(), name='course'),
    url(r'course/(?P<pk>\d+)$', views.courseDetailView.as_view(), name='Данные о курсе'),
    url(r'^teacher/$', views.teacherListView.as_view(), name='teacher'),
    url(r'teacher/(?P<pk>\d+)$', views.teacherDetailView.as_view(), name='Данные о преподавателе')
]
