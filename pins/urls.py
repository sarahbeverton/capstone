from django.urls import path

from pins import views

urlpatterns = [
    path('addpin/', views.AddPinView.as_view(), name="addpin"),
    path('<int:pin_id>/', views.PinView.as_view(), name="pin_detail"),
    path('save/<int:pin_id>/', views.SaveView.as_view()),
    path('remove/<int:pin_id>/', views.RemovePinView.as_view()),
    path('like/<int:pin_id>/', views.like_view)
]
