from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('search/<search_type>/', views.search, name="search"),
    path('regist', csrf_exempt(views.regist), name="regist"),
]
