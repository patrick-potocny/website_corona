from django.urls import path
from . import views

app_name = "counter"

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path("email_request/", views.SignUp.as_view(), name= "email_request"),
    path("email_request/thanks/", views.ThanksPage.as_view(), name= "thanks"),
]