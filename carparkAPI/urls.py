from django.urls import path
from . import views
from .views import carpark, get_token

urlpatterns = [
    path('', carpark, name='carpark'),
    path('token/', get_token, name='token'),
]