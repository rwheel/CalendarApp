from django.urls import path, include
from . import views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path("<int:id>", views.base, name="base"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path('logout/', authentication_views.LogoutView.as_view(template_name='main/home.html'), name='logout'),
]