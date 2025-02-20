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

    # All Dublin regions summarised for Location selection option
    D01 = "Dublin 1"
    D02 = "Dublin 2"
    D03 = "Dublin 3"
    D04 = "Dublin 4"
    D05 = "Dublin 5"
    D06 = "Dublin 6"
    D07 = "Dublin 7"
    D08 = "Dublin 8"
    D09 = "Dublin 9"
    D10 = "Dublin 10"
    D11 = "Dublin 11"
    D12 = "Dublin 12"
    D13 = "Dublin 13"
    D14 = "Dublin 14"
    D15 = "Dublin 15"
    D16 = "Dublin 16"
    D17 = "Dublin 17"
    D18 = "Dublin 18"
    D19 = "Dublin 19"
    D20 = "Dublin 20"
    D21 = "Dublin 21"
    D22 = "Dublin 22"
    D23 = "Dublin 23"
    D24 = "Dublin 24"

    regions_options = [
        (D01, "Dublin 1"),
        (D02, "Dublin 2"),
        (D03, "Dublin 3"),
        (D04, "Dublin 4"),
        (D05, "Dublin 5"),
        (D06, "Dublin 6"),
        (D07, "Dublin 7"),
        (D08, "Dublin 8"),
        (D09, "Dublin 9"),
        (D10, "Dublin 10"),
        (D11, "Dublin 11"),
        (D12, "Dublin 12"),
        (D13, "Dublin 13"),
        (D14, "Dublin 14"),
        (D15, "Dublin 15"),
        (D16, "Dublin 16"),
        (D17, "Dublin 17"),
        (D18, "Dublin 18"),
        (D19, "Dublin 19"),
        (D20, "Dublin 20"),
        (D21, "Dublin 21"),
        (D22, "Dublin 22"),
        (D23, "Dublin 23"),
        (D24, "Dublin 24"),
    ]
    region = models.CharField(max_length=9,
                              choices=regions_options,
                              default=D01)

    # All Dublin regions summarised for Location selection option
    baby = "Baby (age 0-1y)"
    toddler = "Toddler (age 1-3y)"
    child = "Child (age 4-12y)"
    teenager = "Teenager (age 3-19y)"
    youngAdult = "Young adult (age 16-24)"
    multiple = "multiple ages"
    ns = "not specified"

    ages = [        
        (baby, "Baby (age 0-1y)"),
        (toddler, "Toddler (age 1-3y)"),
        (child, "Child (age 4-12y)"),
        (teenager, "Teenager (age 3-19y)"),
        (youngAdult, "Young adult (age 16-24)"),
        (multiple, "Multiple ages"),
        (ns, "Not specified")]
    
    age_group = models.CharField(choices=ages, default=ns)