from django.urls import path

from boards import views

urlpatterns = [
    path('addboard/', views.AddBoardView.as_view()),
    path('<int:board_id>/', views.BoardView.as_view()),
]
