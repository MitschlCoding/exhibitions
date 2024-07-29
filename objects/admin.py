"""This module contains the configuration of the objects apps admin backend."""

from django.contrib import admin

from objects.models import (
    Exhibition,
    Object,
    ObjectDetailSection,
    ObjectDetailSectionImage,
    ObjectDetailSectionText,
)

# Register your models here.

admin.site.register(Exhibition)
admin.site.register(Object)
admin.site.register(ObjectDetailSection)
admin.site.register(ObjectDetailSectionText)
admin.site.register(ObjectDetailSectionImage)
