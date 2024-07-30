"""This module contains the views for the objects app."""

from django.http import HttpResponse
from django.template import loader

from objects.models import Exhibition, Object

# Create your views here.

def exhibition_view(request, exhibition_id):
    """View for an exhibition page."""
    exhibition = Exhibition.objects.get(pk=exhibition_id)
    exhibition_objects = Object.objects.filter(exhibition=exhibition_id)
    context = {
        "exhibition": exhibition,
        "objects": exhibition_objects,
    }
    template = loader.get_template("objects/exhibition.html")
    for exhibition_object in exhibition_objects:
        print(exhibition_object.card_image.url)
    return HttpResponse(template.render(context=context, request=request))


def object_view(request, object_id):
    """View for an object page."""
    exhibition_object = Object.objects.get(pk=object_id)
    context = {
        "exhibition": exhibition_object.exhibition,
        "object": exhibition_object,
    }
    template = loader.get_template("objects/object.html")
    return HttpResponse(template.render(context=context, request=request))
