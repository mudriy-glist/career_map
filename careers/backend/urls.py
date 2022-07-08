from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mecha/", views.mecha, name="mecha"),
    path("woodoo/", views.woodoo, name="woodoo"),
    path("voodoo_newstarter/", views.voodoo_newstarter, name="voodoo_newstarter"),
    path("application_form/", views.application_form, name="application_form")
]