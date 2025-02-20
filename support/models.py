from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Posted"))
REGION = (
    (0, "Not specified"),
    (1, "Dublin 1"),
    (2, "Dublin 2"),
    (3, "Dublin 3"),
    (4, "Dublin 4"),
    (5, "Dublin 5"),
    (6, "Dublin 6"),
    (7, "Dublin 7"),
    (8, "Dublin 8"),
    (9, "Dublin 9"),
    (10, "Dublin 10"),
    (11, "Dublin 11"),
    (12, "Dublin 12"),
    (13, "Dublin 13"),
    (14, "Dublin 14"),
    (15, "Dublin 15"),
    (16, "Dublin 16"),
    (17, "Dublin 17"),
    (18, "Dublin 18"),
    (19, "Dublin 19"),
    (20, "Dublin 20"),
    (21, "Dublin 21"),
    (22, "Dublin 22"),
    (23, "Dublin 23"),
    (24, "Dublin 24"),
)

AGES = (
    (0, "Not specified"),
    (1, "Baby (age 0-1y)"),
    (2, "Toddler (age 1-3y)"),
    (3, "Child (age 4-12y)"),
    (4, "Teenager (age 3-19y)"),
    (5, "Young adult (age 16-24)"),
    (6, "Multiple ages"),
)


# Create your models here.
class Support(models.Model):
    """
    Stores a support post
    """
    topic = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="support_post"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    region = models.CharField(choices=REGION, default=0)
    age_group = models.CharField(choices=AGES, default=0)
