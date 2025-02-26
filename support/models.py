from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Posted")
)


# Create your models here.
class Support(models.Model):
    """
    Stores a support post
    """
    topic = models.CharField(max_length=200, unique=True)
    # Ideally the slug attribute is hidden for users
    slug = models.SlugField(max_length=200, unique=True)
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="support_post"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Region Charfield content
    Dublin_0 = "Not specified"
    Dublin_1 = "Dublin 1"
    Dublin_2 = "Dublin 2"
    Dublin_3 = "Dublin 3"
    Dublin_4 = "Dublin 4"
    Dublin_5 = "Dublin 5"
    Dublin_6 = "Dublin 6"
    Dublin_7 = "Dublin 7"
    Dublin_8 = "Dublin 8"
    Dublin_9 = "Dublin 9"
    Dublin_10 = "Dublin 10"
    Dublin_11 = "Dublin 11"
    Dublin_12 = "Dublin 12"
    Dublin_13 = "Dublin 13"
    Dublin_14 = "Dublin 14"
    Dublin_15 = "Dublin 15"
    Dublin_16 = "Dublin 16"
    Dublin_17 = "Dublin 17"
    Dublin_18 = "Dublin 18"
    Dublin_19 = "Dublin 19"
    Dublin_20 = "Dublin 20"
    Dublin_21 = "Dublin 21"
    Dublin_22 = "Dublin 22"
    Dublin_23 = "Dublin 23"
    Dublin_24 = "Dublin 24"

    REGION = [
        (Dublin_0, "Not specified"),
        (Dublin_1, "Dublin 1"),
        (Dublin_2, "Dublin 2"),
        (Dublin_3, "Dublin 3"),
        (Dublin_4, "Dublin 4"),
        (Dublin_5, "Dublin 5"),
        (Dublin_6, "Dublin 6"),
        (Dublin_7, "Dublin 7"),
        (Dublin_8, "Dublin 8"),
        (Dublin_9, "Dublin 9"),
        (Dublin_10, "Dublin 10"),
        (Dublin_11, "Dublin 11"),
        (Dublin_12, "Dublin 12"),
        (Dublin_13, "Dublin 13"),
        (Dublin_14, "Dublin 14"),
        (Dublin_15, "Dublin 15"),
        (Dublin_16, "Dublin 16"),
        (Dublin_17, "Dublin 17"),
        (Dublin_18, "Dublin 18"),
        (Dublin_19, "Dublin 19"),
        (Dublin_20, "Dublin 20"),
        (Dublin_21, "Dublin 21"),
        (Dublin_22, "Dublin 22"),
        (Dublin_23, "Dublin 23"),
        (Dublin_24, "Dublin 24"),
    ]

    region = models.CharField(choices=REGION, default=Dublin_0, max_length=15)
    
    # age_group Charfield content
    Not_Specified = "Not specified"
    Baby = "Baby (age 0-1y)"
    Toddler = "Toddler (age 1-3y)"
    Child = "Child (age 4-12y)"
    Teenager = "Teenager (age 13-19y)"
    Young_Adult = "Young adult (age 16-24)"
    Multiple_Ages = "Multiple ages"

    AGES = [
        (Not_Specified, "Not specified"),
        (Baby, "Baby (age 0-1y)"),
        (Toddler, "Toddler (age 1-3y)"),
        (Child, "Child (age 4-12y)"),
        (Teenager, "Teenager (age 13-19y)"),
        (Young_Adult, "Young adult (age 16-24)"),
        (Multiple_Ages, "Multiple ages"),
    ]
    age_group = models.CharField(choices=AGES, default=Not_Specified, max_length=30)

    # type_of_request Charfield content
    Not_Specified = "not specified"
    Offering_Help = "Offering help"
    Asking_Help = "Asking help"
    Sharing_Tips_and_Tricks = "Sharing tips & tricks"

    TYPEREQUEST = [
        (Not_Specified, "not specified"),
        (Offering_Help, "Offering help"),
        (Asking_Help, "Asking help"),
        (Sharing_Tips_and_Tricks, "Sharing tips & tricks")
    ]

    type_of_request = models.CharField(
        choices=TYPEREQUEST, default=Not_Specified , max_length=25)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on", "region", "age_group", "type_of_request"]

    def __str__(self):
        return f"{self.region} | {self.type_of_request} | {self.age_group} | Topic: {self.topic}"  #noqa


class Respond(models.Model):
    support = models.ForeignKey(
        Support, on_delete=models.CASCADE, related_name="replies")
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="parent")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Response {self.body} by {self.parent}"
