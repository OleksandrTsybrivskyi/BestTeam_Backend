from django.urls import path
from .views import LocationView, ReviewView

urlpatterns = [
    path('locations/', LocationView.as_view(), name='locations-list'),
    path('reviews/', ReviewView.as_view(), name='reviews-list'),
]
