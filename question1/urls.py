from django.urls import path

from . import views

urlpatterns = [
    path('items/', views.PositiveIntegerStatsView.as_view(), name="positive_integer_stats"),
]
