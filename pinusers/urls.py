from django.urls import path
from pinusers import views

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<str:username>/', views.FollowView.as_view()),
    path('unfollow/<str:username>/', views.UnfollowView.as_view()),
    path('following_pins/<str:username>/', views.following_pins, name='following_pins'),
]