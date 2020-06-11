from django.urls import path
from . import views

urlpatterns = [
        path("", views.top, name="top"),
        path("report", views.report, name="report"),
        path("finds", views.post_list, name="finds"),
        path("login", views.login, name="login"),
]