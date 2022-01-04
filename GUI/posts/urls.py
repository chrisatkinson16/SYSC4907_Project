from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Post-Home'),
    path('live/', views.live, name='Post-Live'),
]
