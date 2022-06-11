import imp
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
# Generic Relationship(Abstract model) -> Ex. using ContentType instead of Product
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag is appied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Using abstract model instead of concrete model
    # We need Type of target object (product, video, article), ID and content object to make generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # Actual object on which the tag is applied
    content_object = GenericForeignKey()
