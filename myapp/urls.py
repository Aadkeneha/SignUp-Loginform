from django.urls import path
from . import views

urlpatterns = [

    path("", views.signup_login, name='signup_login'),
    path("dashboard.html", views.dashboard, name='dashboard'),

]
