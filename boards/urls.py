from django.urls import path

from boards import views

urlpatterns = [
    path('addboard/', views.AddBoardView.as_view()),
    path('<int:board_id>/', views.BoardView.as_view(), name="board"),
    path('<int:board_id>/save/<int:pin_id>', views.SaveToBoardView.as_view()),
]
