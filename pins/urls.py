from django.urls import path

from pins import views

urlpatterns = [
    #path('addpin/', views.AddPinView.as_view()),
    path('<int:pin_id>/', views.PinView.as_view()),
    path('save/<int:pin_id>/', views.SaveView.as_view()),
]
