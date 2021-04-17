from django.urls import path

from . import views

urlpatterns = [
    path('plot/', views.PointView.as_view(), name="plot"),
]
