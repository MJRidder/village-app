from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)

    # type_of_contact Charfield content
    Not_Specified = "not specified"
    Support_Post = "Support post"
    Collaborate = "Collaborate"
    General_Contact = "General contact"

    TYPECONTACT = [
        (Not_Specified, "not specified"),
        (Support_Post, "Support post"),
        (Collaborate, "Collaborate"),
        (General_Contact, "General contact")
    ]

    type_of_request = models.CharField(
        choices=TYPECONTACT,
        default=Not_Specified,
        max_length=16)

    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"