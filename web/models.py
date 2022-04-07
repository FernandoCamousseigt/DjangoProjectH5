from django.db import models
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    is_diet = models.BooleanField(default=False)


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


