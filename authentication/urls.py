from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.LogInView.as_view(), name="login")
]