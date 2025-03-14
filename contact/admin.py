from django.contrib import admin
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """
    Lists received message and read fields for display in admin
    """
    list_display = ('message', 'read',)
