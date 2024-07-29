"""This module contains the URL configuration for the objects app."""

from django.urls import path

from objects import views

urlpatterns = [
    path("exhibition/<int:exhibition_id>/", views.exhibition_view),
    path("object/<int:object_id>/", views.object_view),
]
