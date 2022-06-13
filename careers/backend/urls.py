from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mecha/", views.mecha, name="mecha"),
    path("woodoo/", views.woodoo, name="woodoo")
]