from .api import *
from . import views

from django.urls import path, include

app_name = "url"
urlpatterns = [
    path('api/post',EmployeeCreateApi.as_view()),
    path('api/get',EmployeeApi.as_view()),
   path('api/<pk>',EmployeeUpdateApi.as_view()),
   path("", views.urlShort, name="home"),
    path("u/<str:slugs>", views.urlRedirect, name="redirect")
]