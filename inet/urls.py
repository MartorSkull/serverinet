from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('search/<search_type>/', views.search, name="search"),
]
