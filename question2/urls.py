from django.urls import path

from . import views

urlpatterns = [
    path('booking/', views.BookingView.as_view(), name="booking"),
    path('cancel/', views.CancelView.as_view(), name="cancel")
]
