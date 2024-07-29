from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from objects.models import Object, Exhibition

# Create your views here.

def exhibition(request, exhibition_id):
    exhibition = Exhibition.objects.get(pk=exhibition_id)
    objects = Object.objects.filter(exhibition=exhibition_id)
    context = {
        "exhibition": exhibition,
        "objects": objects,
    }
    template = loader.get_template("objects/exhibition.html")
    for object in objects:
        print(object.card_image.url)
    return HttpResponse(template.render(context=context, request=request))

def object(request, object_id):
    object = Object.objects.get(pk=object_id)
    context = {
        "exhibition": object.exhibition,
        "object": object,
    }
    template = loader.get_template("objects/object.html")
    return HttpResponse(template.render(context=context, request=request))