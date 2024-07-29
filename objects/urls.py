from django.urls import path

from objects import views

urlpatterns = [
    path("exhibition/<int:exhibition_id>/", views.exhibition),
    path("object/<int:object_id>/", views.object),
]