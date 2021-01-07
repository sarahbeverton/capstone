from django.urls import path
from pinusers import views

urlpatterns = [
    path('profile/', views.profile, name='profile')
]
