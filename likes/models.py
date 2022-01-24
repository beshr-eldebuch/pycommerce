from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Like(models.Model):
    quantity = models.PositiveBigIntegerField()

class LikedItem(models.Model):
    like = models.ForeignKey(Like, on_delete=models.CASCADE)    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey