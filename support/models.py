from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))


# Create your models here.
class Support(models.Model):
    """
    Stores a support post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="support_post"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
