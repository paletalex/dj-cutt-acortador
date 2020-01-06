from django.urls import path 
from .views import Home, SuccessDeatil

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("<str:key>/", SuccessDeatil.as_view(), name="success"),
]
