from django.urls import path
from . import views

urlpatterns = [
    # The URL pattern for handling shortened URLs
    path('<str:alias>/', views.redirect_to_url, name='redirect_to_url'),
]
