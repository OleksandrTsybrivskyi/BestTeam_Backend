from django.urls import path
from .views import LocationView, ReviewView, RegisterView, ProposalView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('locations/', LocationView.as_view(), name='locations-list'),
    path('reviews/', ReviewView.as_view(), name='reviews-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('proposal/', ProposalView.as_view(), name='proposals-list')
]
