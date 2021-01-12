from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.LogInView.as_view(), name="login"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
]


handler404 = 'authentication.views.error_view'
handler500 = 'authentication.views.server_error_view'
