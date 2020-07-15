from django.urls import path
from . import views

app_name = "counter"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
]