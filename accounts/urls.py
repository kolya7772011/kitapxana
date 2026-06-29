from django.urls import path
from .views import RegisterCreateView

urlpatterns = [
    path('login/', RegisterCreateView.as_view())
]