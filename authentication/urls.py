from django.urls import path
import django

from authentication import views


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


def custom_server_error(request):
    return django.views.defaults.server_error(request)


urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.LogInView.as_view(), name="login"),
    path('logout/', views.LogOutView.as_view(), name="logout"),
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),
]


handler404 = 'authentication.views.error_view'
handler500 = 'authentication.views.server_error_view'
