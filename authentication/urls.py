from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
]