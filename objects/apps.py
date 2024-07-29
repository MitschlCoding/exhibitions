"""This module contains the configuration of the objects app.
The Objects app is a simple Django app for building a Museum Exhibition website."""

from django.apps import AppConfig


class ObjectsConfig(AppConfig):
    """Configuration for the objects app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "objects"
