from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttpes.models import ContentType
from django.contrib.contenttpes.fields import GenericForeignKeys 

# Create your models here.
class LikedItem(models.Model):
    User= models.ForeignKeys(User, on_delete=models.CASCADE)
    content_type = models.ForeignKeys(c=ContentType, on_delete=model.CASCADE)
    object_id= models.PositiveIntegerField()
    conent_object = GenericForeignKeys()