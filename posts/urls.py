from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Post-Home'),
    path('live/', views.live, name='Post-Live'),
    path('recommendation/', views.recommendation, name='Post-Recommendation'),
    path('social/', views.social, name='Post-Social'),
    path('capacity/', views.capacity, name='Post-Capacity'),
]
