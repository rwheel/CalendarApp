from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import views as authentication_views

app_name = 'main'
urlpatterns = [
    path("<int:id>", views.base, name="base"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path('logout/', authentication_views.LogoutView.as_view(template_name='main/home.html'), name='logout'),
    url('index', views.index, name='index'),
    url('calendar/', views.CalendarView.as_view(), name='calendar'),
    url('event/new/', views.event, name='event_new'),
    url('event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]