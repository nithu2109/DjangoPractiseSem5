from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("emp_post/", views.emp_post, name="emp_post"),
]
