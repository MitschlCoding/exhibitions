"""Models for the objects app."""

from django.db import models

# Create your models here.


class Exhibition(models.Model):
    """An exhibition models a museum exhibition. It has a name, subline, description,
    banner image, description image, and accent color. And contains a collection of objects.
    """

    name = models.CharField(max_length=100)
    subline = models.CharField(max_length=100)
    description_headline = models.CharField(max_length=100)
    description = models.TextField()
    banner_image = models.ImageField(upload_to="images/")
    description_image = models.ImageField(upload_to="images/", default=None, null=True)
    accent_color = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Object(models.Model):
    """An object models an object in a museum exhibition. It has a name, subline, description,
    banner image, and card image. And belongs to an exhibition."""

    exhibition = models.ForeignKey(
        Exhibition, on_delete=models.CASCADE, default=None, null=True
    )
    name = models.CharField(max_length=100)
    subline = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to="images/", default=None, null=True)
    description = models.TextField()
    card_image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class ObjectDetailSection(models.Model):
    """An object detail section models a section of an object detail page on the generated
    website. It has a title, position, and type. And belongs to an object."""

    object_detail_page = models.ForeignKey(Object, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pos = models.IntegerField(default=0)

    class Template(models.TextChoices):
        """Template tells the website how to render the object detail section."""

        TEXT = "TEXT", "Text"
        IMAGE = "IMAGE", "Image"
        IMAGE_TEXT = "IMAGE_TEXT", "Image and Text"
        TEXT_IMAGE = "TEXT_IMAGE", "Text and Image"
        TEXT_ON_IMAGE = "TEXT_ON_IMAGE", "Text on Image"
        IMAGE_SLIDER = "IMAGE_SLIDER", "Image Slider"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class ObjectDetailSectionText(models.Model):
    """An object detail section text models a text section of an object detail section on
    the generated website. It has text. And belongs to an object detail section."""

    object_detail_section = models.ForeignKey(
        ObjectDetailSection, on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)


class ObjectDetailSectionImage(models.Model):
    """An object detail section image models an image section of an object detail section
    on the generated website. It has an image and alt text. And belongs to an object detail
    section."""

    object_detail_section = models.ForeignKey(
        ObjectDetailSection, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/")
    alt_text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.alt_text)
